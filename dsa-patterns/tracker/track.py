#!/usr/bin/env python3
"""Local DSA tracker; optional public LeetCode snapshot. No account credentials."""
import argparse
from datetime import datetime, timedelta
import json
from pathlib import Path
import sys
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
STATE = HERE / 'progress.json'
REPORT = HERE.parent / 'TRACKER.md'
STATUSES = ('not_recorded', 'attempted', 'with_help', 'independent', 'reviewed')
LABELS = {'not_recorded': 'Not recorded', 'attempted': 'Attempted', 'with_help': 'Solved with help', 'independent': 'Independent solve', 'reviewed': 'Reviewed'}
QUERY = '''query PublicProgress($username: String!, $limit: Int!) {
  matchedUser(username: $username) {
    username
    submitStatsGlobal { acSubmissionNum { difficulty count submissions } }
  }
  recentAcSubmissionList(username: $username, limit: $limit) {
    id title titleSlug timestamp
  }
}'''


def cell(value):
    return str(value or '—').replace('|', '\\|').replace('\n', '<br>')


def now_for(state):
    return datetime.now(ZoneInfo(state['timezone']))


def sync_public(state, now):
    sync = state['sync']
    sync['last_attempt'] = now.isoformat(timespec='seconds')
    payload = json.dumps({'query': QUERY, 'variables': {'username': state['profile']['username'], 'limit': sync['history_limit']}}).encode()
    request = urllib.request.Request('https://leetcode.com/graphql/', payload, {
        'Content-Type': 'application/json', 'User-Agent': 'DSAPreparationTracker/1.0',
        'Referer': state['profile']['url']})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            body = json.load(response)
        if body.get('errors'):
            raise ValueError('; '.join(error.get('message', 'GraphQL error') for error in body['errors']))
        data = body.get('data') or {}
        user = data.get('matchedUser')
        if not user:
            raise ValueError('Profile not found or public statistics unavailable')
        recent = data.get('recentAcSubmissionList')
        if not isinstance(recent, list):
            raise ValueError('Recent accepted submissions unavailable')
        stats = {row['difficulty']: row['count'] for row in user['submitStatsGlobal']['acSubmissionNum']}
        recent = [{'id': str(row['id']), 'title': row['title'], 'slug': row['titleSlug'],
                   'date': datetime.fromtimestamp(int(row['timestamp']), ZoneInfo(state['timezone'])).date().isoformat()}
                  for row in recent]
        # Only positively observed acceptances are imported. Absence does not mean unsolved.
        observed = {row['slug'] for row in recent}
        for problem in state['problems']:
            if problem['slug'] in observed:
                problem['accepted'] = True
        sync.update(status='public_snapshot', last_success=now.isoformat(timespec='seconds'),
                    error=None, statistics=stats, recent_accepted=recent)
        return True
    except (urllib.error.URLError, ValueError, KeyError, TypeError, TimeoutError, OSError) as error:
        # Keep prior statistics and manual progress if a refresh fails.
        sync['status'] = 'refresh_failed'
        sync['error'] = f'{type(error).__name__}: {error}'
        return False


def render(state, today):
    patterns = state['patterns']; problems = state['problems']; sync = state['sync']
    complete = sum(all(p['checkpoints'].values()) for p in patterns)
    checkpoints = sum(sum(p['checkpoints'].values()) for p in patterns)
    independent = sum(p['practice_status'] in ('independent', 'reviewed') for p in problems)
    accepted = sum(p['accepted'] is True for p in problems)
    due = [p for p in problems if p['review_due'] and p['review_due'] <= today]
    lines = ['# DSA progress tracker', '', '[Preparation roadmap](README.md) · [LeetCode profile]('+state['profile']['url']+')', '',
             'Your study tracker covers 20 patterns and 34 unique practice problems. Unchecked checkpoints and “Not recorded” mean no progress has been recorded here; they do not imply you have never studied or solved the topic.', '',
             '## Progress recorded here', '',
             f'- Patterns with all four checkpoints: **{complete}/20**.',
             f'- Learning checkpoints completed: **{checkpoints}/80**.',
             f'- Problems independently solved or reviewed: **{independent}/34**.',
             f'- Practice problems with an accepted submission positively observed: **{accepted}/34**; other acceptance statuses remain unknown.',
             f'- Reviews due: **{len(due)}**.', '',
             'An accepted submission does not prove an independent solve. Public sync never changes your learning checkpoints, independence rating, notes, or review dates.', '',
             '## LeetCode connection', '',
             '- Mode: **public read-only snapshot**, refreshed on demand with `python3 dsa-patterns/tracker/track.py --sync`.',
             '- Authenticated account connection: **not configured**. No LeetCode credentials or session cookies are stored.',
             '- Latest refresh state: **'+cell(sync['status'])+'**.',
             '- Last successful snapshot: '+cell(sync['last_success'])+'.',
             '- Last refresh attempt: '+cell(sync['last_attempt'])+'.',
             '- A native LeetCode connector was not found in the available plugin search. More integrations may be available in the [plugin directory](https://chatgpt.com/plugins). Public GraphQL availability may change; an unsuccessful refresh preserves saved progress.', '']
    if sync['error']:
        lines += ['Latest refresh error: `'+str(sync['error']).replace('`', "'")+'`.', '']
    if sync['statistics']:
        lines += ['| Public solved count | Value |','| --- | --- |']
        for key in ('All','Easy','Medium','Hard'):
            lines.append('| '+key+' | '+str(sync['statistics'].get(key, 'Unavailable'))+' |')
        lines += ['','These are profile-wide statistics, separate from this 34-problem plan.','']
    else:
        lines += ['Public solved totals are **not verified yet**; no account statistics have been guessed.','']
    lines += ['The endpoint returns only a limited recent accepted list (up to 20 entries requested here), not a full solved-problem inventory. Older solved problems can remain “Unknown”; mark them manually when appropriate.', '',
              '## Next session', '',
              '1. Re-solve a due review without opening the solution, if any are due.',
              '2. Otherwise use the first incomplete guide below.',
              '3. Read → reproduce its dry run → write Java from memory → explain the invariant and complexity.',
              '4. Attempt one linked problem and record whether you needed help.', '']
    by_id = {p['id']: p for p in patterns}
    next_pattern = next((by_id[i] for i in state['study_order'] if not all(by_id[i]['checkpoints'].values())), None)
    if next_pattern:
        lines += ['Next incomplete guide: **['+next_pattern['title']+']('+next_pattern['guide']+')**.', '']
    lines += ['## Pattern checkpoints', '',
              'Read = understand recognition and state. Dry run = reproduce its table without looking. Java = implement from memory. Explain = justify correctness and complexity. A pattern is complete here only when all four are checked; problem mastery is tracked separately.', '',
              '| ID | Pattern | Read | Dry run | Java | Explain | Notes |',
              '| --- | --- | --- | --- | --- | --- | --- |']
    for identifier in state['study_order']:
        p = by_id[identifier]; flags = ['[x]' if p['checkpoints'][k] else '[ ]' for k in ('read','dry_run','java','explain')]
        lines.append('| '+p['id']+' | ['+p['title']+']('+p['guide']+') | '+' | '.join(flags)+' | '+cell(p['notes'])+' |')
    lines += ['', '## Review queue', '']
    scheduled = sorted((p for p in problems if p['review_due']), key=lambda p:(p['review_due'],p['id']))
    if scheduled:
        lines += ['| Due | Problem | Due now? | Completed reviews |','| --- | --- | --- | --- |']
        for p in scheduled:
            lines.append('| '+p['review_due']+' | ['+str(p['id'])+'. '+p['title']+']('+p['url']+') | '+('Yes' if p['review_due'] <= today else 'No')+' | '+str(p['reviews'])+' |')
    else:
        lines += ['No reviews scheduled yet. A recorded attempt or solve schedules a next-day retry/review. Successful reviews then use intervals of 3, 7, 14, and 30 days. Recording an attempt or a solve with help resets that problem’s review progression.']
    lines += ['', '## Problem tracker', '',
              'Practice statuses: Not recorded → Attempted → Solved with help / Independent solve → Reviewed. “Reviewed” means you re-solved from memory. LeetCode AC is a separate acceptance observation; unknown is not unsolved.', '',
              '| Problem | Pattern IDs | Practice status | LeetCode AC | Last practiced | Review due | Notes |',
              '| --- | --- | --- | --- | --- | --- | --- |']
    for p in problems:
        ac = 'Observed' if p['accepted'] is True else 'Unknown'
        notes = ('Premium question. ' if p['premium'] else '') + p['notes']
        lines.append('| ['+str(p['id'])+'. '+p['title']+']('+p['url']+') | '+', '.join(p['patterns'])+' | '+LABELS[p['practice_status']]+' | '+ac+' | '+cell(p['last_practiced'])+' | '+cell(p['review_due'])+' | '+cell(notes)+' |')
    lines += ['', '## Recent accepted activity', '']
    if sync['recent_accepted']:
        lines += ['| Date ('+state['timezone']+') | Problem |','| --- | --- |']
        for row in sync['recent_accepted']:
            lines.append('| '+row['date']+' | ['+row['title']+'](https://leetcode.com/problems/'+row['slug']+'/) |')
    else:
        lines += ['No recent accepted activity has been imported yet.']
    lines += ['', '## Update your tracker', '',
              'Ask the assistant to record progress, edit `tracker/progress.json`, or run the commands below from the project root. This Markdown report is generated: edit the JSON instead of changing its table/checkmarks directly, then render again.', '',
              '```sh',
              '# Regenerate this report without network access',
              'python3 dsa-patterns/tracker/track.py', '',
              '# Mark the four learning checkpoints for pattern 01',
              'python3 dsa-patterns/tracker/track.py --pattern 01 --check read,dry_run,java,explain', '',
              '# Record an independent solve; dates default to today in Asia/Kolkata',
              'python3 dsa-patterns/tracker/track.py --problem 283 --status independent --notes "Read/write invariant"', '',
              '# Record a later successful re-solve and advance its review interval',
              'python3 dsa-patterns/tracker/track.py --problem 283 --status reviewed', '',
              '# Refresh publicly available profile statistics and recent acceptances',
              'python3 dsa-patterns/tracker/track.py --sync',
              '```', '',
              'Use `--accepted` only when you know the problem has an accepted submission. Use `--uncheck read` with `--pattern` to clear a checkpoint. `--date YYYY-MM-DD` records a past practice date. `--help` lists all options. Refreshes run only when requested; no background automation has been scheduled.', '']
    return '\n'.join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sync', action='store_true', help='Fetch public statistics and a recent accepted snapshot')
    parser.add_argument('--pattern', help='Pattern ID, 01 through 20')
    parser.add_argument('--check', help='Comma-separated read,dry_run,java,explain checkpoints to mark')
    parser.add_argument('--uncheck', help='Comma-separated checkpoints to clear')
    parser.add_argument('--problem', help='LeetCode numeric ID or slug')
    parser.add_argument('--status', choices=STATUSES)
    parser.add_argument('--accepted', action='store_true', help='Manually record a known accepted submission')
    parser.add_argument('--notes', help='Replace notes for the selected pattern or problem')
    parser.add_argument('--date', help='Practice date YYYY-MM-DD (defaults to today)')
    args = parser.parse_args(argv)
    state = json.loads(STATE.read_text()); now = now_for(state); today = now.date()
    if args.pattern and args.problem: parser.error('Select a pattern or a problem, not both')
    if (args.check or args.uncheck) and not args.pattern: parser.error('Checkpoint changes require --pattern')
    if (args.status or args.accepted or args.date) and not args.problem: parser.error('Practice updates require --problem')
    if args.notes is not None and not (args.pattern or args.problem): parser.error('Notes require --pattern or --problem')
    if args.pattern:
        pattern = next((p for p in state['patterns'] if p['id'] == args.pattern.zfill(2)), None)
        if pattern is None: parser.error('Unknown pattern')
        for values, flag in ((args.check, True), (args.uncheck, False)):
            if values:
                for key in values.split(','):
                    if key not in pattern['checkpoints']: parser.error('Unknown checkpoint: '+key)
                    pattern['checkpoints'][key] = flag
        if args.notes is not None: pattern['notes'] = args.notes
    if args.problem:
        problem = next((p for p in state['problems'] if str(p['id']) == args.problem or p['slug'] == args.problem), None)
        if problem is None: parser.error('Problem is not in the preparation plan')
        try: practice_date = datetime.strptime(args.date, '%Y-%m-%d').date() if args.date else today
        except ValueError: parser.error('Use a valid YYYY-MM-DD practice date')
        if practice_date > today: parser.error('Practice date cannot be in the future')
        if args.date and not args.status: parser.error('--date requires a practice --status')
        if args.status:
            if args.status == 'reviewed' and problem['practice_status'] not in ('with_help','independent','reviewed'):
                parser.error('Record an initial solve before recording a review')
            problem['practice_status'] = args.status
            if args.status == 'not_recorded':
                problem.update(last_practiced=None, review_due=None, reviews=0)
            else:
                problem['last_practiced'] = practice_date.isoformat()
                if args.status == 'reviewed':
                    problem['reviews'] += 1
                    interval = (3,7,14,30)[min(problem['reviews']-1,3)]
                else:
                    problem['reviews'] = 0; interval = 1
                problem['review_due'] = (practice_date + timedelta(days=interval)).isoformat()
        if args.accepted: problem['accepted'] = True
        if args.notes is not None: problem['notes'] = args.notes
    success = sync_public(state, now) if args.sync else True
    STATE.write_text(json.dumps(state, indent=2)+'\n')
    REPORT.write_text(render(state, today.isoformat()))
    print('Updated '+str(REPORT))
    if args.sync:
        print('Public profile refresh succeeded.' if success else 'Public profile refresh failed: '+state['sync']['error'])
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
