# System-design progress tracker

[Four-week plan](README.md) · [Design template and rubric](DESIGN_TEMPLATE.md)

Budget: 28 sessions of one hour, split equally between App and Platform. Check a session only after producing its deliverable. No sessions or readiness scores are prefilled. Dates are yours to record; day numbers are relative.

## Daily sessions

### Week 1

- [ ] **Day 01 — App: Baseline: design the RedRail booking funnel.** One baseline diagram, five assumptions, and an initial self-score.
- [ ] **Day 02 — Platform: Android execution and process lifecycle.** One interaction sequence with thread/process ownership.
- [ ] **Day 03 — App: Offline-first railway data and synchronization.** Read/write sequences plus a small local schema.
- [ ] **Day 04 — Platform: Binder/AIDL service design.** Interface sketch and normal/dead-peer sequences.
- [ ] **Day 05 — App: Versioned server-driven UI.** Schema example, fallback policy, and rollout decision.
- [ ] **Day 06 — Platform: Performance investigation as a design process.** Hypothesis-to-evidence table with one counter-hypothesis.
- [ ] **Day 07 — App: Mock 1: booking funnel with process death.** Timed mock score and top two gaps.

### Week 2

- [ ] **Day 08 — Platform: Process importance and memory pressure.** Policy decision table, two counterexamples, and safety fallback.
- [ ] **Day 09 — App: Real-time auction client.** Event schema and reconnect sequence with cursor/gap recovery.
- [ ] **Day 10 — Platform: Live IPC topology graph.** Graph schema, update pipeline, and loss/rebuild policy.
- [ ] **Day 11 — App: Booking/payment consistency.** State machine covering timeout, duplicate retry, and late success.
- [ ] **Day 12 — Platform: Device telemetry collection pipeline.** Data-flow diagram and explicit loss/retention decisions.
- [ ] **Day 13 — App: Modular Android app and dynamic feature delivery.** Module graph and plan for feature download failure.
- [ ] **Day 14 — Platform: Mock 2: dependency-aware process policy.** Timed mock score and evidence for policy guardrails.

### Week 3

- [ ] **Day 15 — App: Offline asset delivery and database migration.** Lifecycle diagram and interrupted-update recovery steps.
- [ ] **Day 16 — Platform: Startup and Compose jank investigation.** Experiment matrix with metrics, controls, and regression checks.
- [ ] **Day 17 — App: Notifications, background sync, and process recreation.** Background-work decision table and reopen-after-death sequence.
- [ ] **Day 18 — Platform: LLM-assisted Perfetto analysis tool.** Pipeline, evaluation rubric, and behavior on unsupported conclusions.
- [ ] **Day 19 — App: SDUI incident response and architecture evolution.** One incident timeline plus a staged rollback plan.
- [ ] **Day 20 — Platform: Reliable privileged service under overload.** AIDL-level contract, thread/lock diagram, and overload policy.
- [ ] **Day 21 — App: Mock 3: real-time auction with reconnect and duplicate bids.** Timed mock score and comparison with Mock 1.

### Week 4

- [ ] **Day 22 — Platform: Mock 4: fleet performance monitoring.** Timed mock score, data-loss budget, and rollback trigger.
- [ ] **Day 23 — App: Resume defense: RedRail/offline/SDUI.** Two five-minute story outlines; mark facts still needing verification.
- [ ] **Day 24 — Platform: Resume defense: process policy/performance/IPC graph.** Two five-minute story outlines plus benchmark methodology.
- [ ] **Day 25 — App: Repair weakest app design and change one constraint.** Revised design and one explicit tradeoff reversal.
- [ ] **Day 26 — Platform: Repair weakest platform design and inject failure.** Failure sequence and a quantitative verification plan.
- [ ] **Day 27 — App: Mock 5: offline-first travel app with booking recovery.** Final app score and remaining interview-day reminders.
- [ ] **Day 28 — Platform: Mock 6: IPC graph feeding a safe process policy.** Final platform score and remaining interview-day reminders.

## Mock scores

Each dimension is scored 1–4; totals are out of 24. Use the [rubric](DESIGN_TEMPLATE.md#self-scoring-rubric); record observations rather than a guessed score.

| Day | Track | Date | Scope | Boundaries | Contracts/data | Correctness/failures | Performance/evidence | Tradeoffs/rollout | Total | Next correction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 07 | App | — | — | — | — | — | — | — | Not assessed | — |
| 14 | Platform | — | — | — | — | — | — | — | Not assessed | — |
| 21 | App | — | — | — | — | — | — | — | Not assessed | — |
| 22 | Platform | — | — | — | — | — | — | — | Not assessed | — |
| 27 | App | — | — | — | — | — | — | — | Not assessed | — |
| 28 | Platform | — | — | — | — | — | — | — | Not assessed | — |

## Resume narratives

- [ ] App architecture: scope, ownership, alternative, outcome, evidence.
- [ ] Offline asset/data lifecycle: compressed size versus installed cost, migration, recovery.
- [ ] Process policy / IPC graph: identity, correctness, overhead, safe rollback.
- [ ] Performance diagnosis: metric definition, baseline, controls, uncertainty.

## Gap log

| Date/session | Observation | Why it matters | Next drill | Rechecked? |
| --- | --- | --- | --- | --- |
| — | No assessment recorded yet | — | — | — |

## End-of-plan review

- [ ] Final app mock evaluated against all six rubric dimensions.
- [ ] Final platform mock evaluated against all six dimensions.
- [ ] Each final mock reaches the personal target of 18/24, with no dimension below 2 and correctness/failure handling at least 3.
- [ ] At least four resume narratives are factual and clearly distinguish personal contribution from team results.
- [ ] Weak areas have a concrete next drill, rather than only “read more.”

Do not infer completion from reading a chapter. Evidence is a design you can explain, challenge, and revise without copying the reference.
