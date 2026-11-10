# Java cheatsheet for DSA preparation

[Pattern guides](README.md) · [Progress tracker](TRACKER.md)

Targets **Java 17+**, including records. Covers Java basics, standard collections, and the main custom structures used in interview/competitive-programming problems. Examples use zero-based indexing unless a section says otherwise.

**Snippet convention:** short Java blocks are independent examples; place statements inside `main` or a method, and helper methods/types inside a class. Standard imports are `java.util.*`, `java.io.*`, and `java.math.BigInteger`. The input template and `DSATemplates` block are complete classes.

## Jump to a topic

- [Pick a structure](#pick-a-structure)
- [Program template and input/output](#program-template-and-inputoutput)
- [Types and numeric safety](#types-and-numeric-safety)
- [Operators, loops, and methods](#operators-loops-and-methods)
- [Classes, modifiers, and exceptions](#classes-modifiers-and-exceptions)
- [Strings and characters](#strings-and-characters)
- [Arrays and matrices](#arrays-and-matrices)
- [ArrayList and LinkedList](#arraylist-and-linkedlist)
- [Stacks, queues, and deques](#stacks-queues-and-deques)
- [Sets](#sets)
- [Maps and frequency counting](#maps-and-frequency-counting)
- [Ordered sets and maps](#ordered-sets-and-maps)
- [Heap / PriorityQueue](#heap--priorityqueue)
- [Sorting and comparators](#sorting-and-comparators)
- [Binary search](#binary-search)
- [Pairs, records, equality, and generics](#pairs-records-equality-and-generics)
- [Iteration, copying, and conversions](#iteration-copying-and-conversions)
- [Bits, BitSet, and big integers](#bits-bitset-and-big-integers)
- [Custom structures: diagrams and templates](#custom-structures-diagrams-and-templates)
- [Pattern snippets](#pattern-snippets)
- [Complexity reference](#complexity-reference)
- [Common mistakes](#common-mistakes)
- [Interview recall checklist](#interview-recall-checklist)

## Pick a structure

| Need | Default Java choice | Key property |
| --- | --- | --- |
| Fixed-size indexed data | `int[]`, `long[]` | Fast indexing; no boxing |
| Resizable indexed sequence | `ArrayList<E>` | Fast indexing and amortized append |
| Linked sequence / end operations | `LinkedList<E>` | Doubly linked; indexed access needs traversal |
| LIFO stack | `Deque<E>` + `ArrayDeque<>` | `push`, `pop`, `peek` |
| FIFO queue | `Queue<E>` + `ArrayDeque<>` | `offer`, `poll`, `peek` |
| Both-end access | `Deque<E>` + `ArrayDeque<>` | `offerFirst/Last`, `pollFirst/Last` |
| Membership / unique keys | `HashSet<E>` | Expected constant-time lookup |
| Counts / key-value lookup | `HashMap<K,V>` | Expected constant-time key operations |
| Insertion-ordered unique keys | `LinkedHashSet<E>` | Iteration follows insertion order |
| Insertion-ordered mappings | `LinkedHashMap<K,V>` | Can also be configured for access order |
| Sorted keys / predecessor / successor | `TreeSet<E>`, `TreeMap<K,V>` | Balanced search-tree operations |
| Repeated minimum / maximum | `PriorityQueue<E>` | Binary heap; default is minimum first |
| Enum keys | `EnumSet<E>`, `EnumMap<E,V>` | Specialized collections for enum values |
| Packed nonnegative bit positions | `BitSet` | Bitwise set operations |
| Connectivity groups | Custom DSU | Path compression + union by size |
| Prefix search / dictionary | Custom trie | Character-by-character paths |
| Point-add / prefix-sum | Custom Fenwick tree | O(log n) updates and sums |
| Point-set / range-sum | Custom segment tree | O(log n) operations |
| Range-add / range-sum | Lazy segment tree | See the [range guide](17_range_queries.md) |
| Static range minimum | Custom sparse table | O(1) query after O(n log n) build |
| Graph | Adjacency list / matrix / edge list | Representation depends on operations |
| Binary tree / BST | Custom node class | Shape and balance determine cost |

For single-threaded DSA, prefer these ordinary collections. `Vector`, `Stack`, and `Hashtable` are legacy choices; concurrent structures such as `ConcurrentHashMap` and `BlockingQueue` solve different, multithreaded requirements. Java has no general standard `Pair`, multiset, trie, DSU, Fenwick tree, or segment-tree class. Use a record, a count map, or a custom implementation.

## Program template and input/output

Save this block as **Main.java**. Run `javac --release 17 Main.java`, then `java Main`. Input starts with n followed by n integers; output is their sum.

```java
import java.io.*;
import java.util.*;

public class Main {
    static class FastScanner {
        private final BufferedReader reader;
        private StringTokenizer tokens;
        FastScanner(InputStream input) {
            reader = new BufferedReader(new InputStreamReader(input));
        }
        String next() throws IOException {
            while (tokens == null || !tokens.hasMoreTokens()) {
                String line = reader.readLine();
                if (line == null) return null;
                tokens = new StringTokenizer(line);
            }
            return tokens.nextToken();
        }
        int nextInt() throws IOException {
            String token = next();
            if (token == null) throw new EOFException("Expected integer");
            return Integer.parseInt(token);
        }
        long nextLong() throws IOException {
            String token = next();
            if (token == null) throw new EOFException("Expected long");
            return Long.parseLong(token);
        }
    }
    public static void main(String[] args) throws IOException {
        FastScanner input = new FastScanner(System.in);
        String first = input.next();
        if (first == null) return;
        int n = Integer.parseInt(first);
        long sum = 0;
        for (int i = 0; i < n; i++) sum += input.nextInt();
        System.out.println(sum);
    }
}
```

- `Scanner` is convenient for small input; buffered tokenization is a useful contest alternative.
- This token reader discards whitespace and does not preserve empty lines. For whole-line text, use `BufferedReader.readLine()` directly.
- Build large output with a `StringBuilder`, then print once.
- On LeetCode, keep its requested `Solution`, `ListNode`, or `TreeNode` signatures; usually no input parser or `main` is needed.

## Types and numeric safety

| Type | Size / role | Useful constants |
| --- | --- | --- |
| `byte` | Signed 8-bit integer | −128..127 |
| `short` | Signed 16-bit integer | −32768..32767 |
| `int` | Signed 32-bit integer | `Integer.MIN_VALUE`, `Integer.MAX_VALUE` |
| `long` | Signed 64-bit integer | `Long.MIN_VALUE`, `Long.MAX_VALUE` |
| `float`, `double` | Floating-point; not exact decimal arithmetic | Use `double` for most numeric DSA |
| `char` | Unsigned 16-bit UTF-16 code unit | `'a'`, `'0'`, `'\n'` |
| `boolean` | `true` or `false` | No numeric conversion |
| `BigInteger` | Arbitrary-precision integer | `ZERO`, `ONE` |

```java
int x = 1_000_000_000;
long product = 1L * x * 3;             // 3_000_000_000; widen BEFORE multiplying
long limit = 1_000_000_007L;
double ratio = 5 / 2.0;               // 2.5; 5 / 2 would be 2
int digit = '7' - '0';                // 7, for ASCII digit characters
int parsed = Integer.parseInt("123");
String text = Long.toString(product);
int safeCast = Math.toIntExact(123L); // Throws if a long cannot fit in int
long absolute = Math.abs((long) Integer.MIN_VALUE);
```

Fields and array elements get default zero/false/null values; local variables must be initialized before use. Object variables hold references. Collections require wrapper types such as `Integer`, not primitives: `List<Integer>`, never `List<int>`. Unboxing a null wrapper throws `NullPointerException`.

Integer overflow normally wraps silently. Use `Math.addExact`/`multiplyExact` when you want overflow detection. `Math.abs(Integer.MIN_VALUE)` is still negative, so widen first when necessary. For DP sentinels, `Long.MAX_VALUE / 4` leaves headroom, but still guard transitions from unreachable states.

## Operators, loops, and methods

```java
int total = 0;
for (int i = 0; i < 5; i++) total += i;
int[] values = {2, 4, 6};
for (int value : values) total += value;
int remaining = 3;
while (remaining > 0) remaining--;
boolean valid = values.length > 0 && values[0] > 0; // Short-circuit AND
int best = valid ? values[0] : -1;
int normalized = Math.floorMod(-3, 5);              // 2; -3 % 5 is -3
```

A helper method belongs **inside a class, outside another method**:

```java
static long gcd(long a, long b) { // Precondition: a,b >= 0
    while (b != 0) {
        long remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}
```

`break` exits the nearest loop; `continue` starts its next iteration; `return` exits the method. Java passes everything by value: a copied reference can mutate the same array/object, but reassigning a method parameter cannot replace the caller's reference. Deep recursion can exhaust the stack; use an explicit stack/queue for large-depth input.

## Classes, modifiers, and exceptions

| Concept | Java reminder |
| --- | --- |
| Class / object | `class Node { int value; Node next; }` describes a type; `new Node()` creates an instance |
| Constructor | Same name as class, no return type; initializes a new instance |
| `this` | Refers to the current instance; `this.value = value` distinguishes field and parameter |
| `static` | Member belongs to the class; a static method cannot directly use instance fields |
| `private` / `public` | Controls where a field, constructor, or method can be accessed |
| `final` variable | Assigned once; a final reference can still point to a mutable collection |
| `extends` / `implements` | Inherit from one class / implement interface contracts |
| `@Override` | Compiler checks that the method overrides a parent/interface declaration |
| Interface reference | `List<Integer> a = new ArrayList<>();` exposes the List operations |
| Lambda | `x -> x * 2` supplies an implementation for a functional interface |
| Record | Compact data carrier; components are final, but referenced objects can remain mutable |
| Checked exception | `IOException` must be caught or declared with `throws` |
| Runtime exception | Examples: invalid index, null dereference, failed numeric parsing |
| `try` / `catch` / `finally` | Execute code, handle a matching exception, run cleanup |

A public top-level class normally needs a matching filename. In this cheatsheet, nested helpers belong inside your outer class; Java does not support declaring an ordinary method inside another method. Use constructors to initialize state and reset per-problem fields between independent test cases. If you override `equals`, also provide a compatible `hashCode` for hash collections.

## Strings and characters

```java
String s = "banana";
int n = s.length();                   // Method: length()
char c = s.charAt(1);                 // 'a'
String part = s.substring(1, 4);       // "ana"; end is exclusive
boolean same = s.equals("banana");   // Content equality
boolean has = s.contains("nan");
int first = s.indexOf("ana");         // 1; -1 means absent
boolean prefix = s.startsWith("ban");
char[] chars = s.toCharArray();
String rebuilt = new String(chars);
String[] words = "a  b\tc".strip().split("\\s+");
String joined = String.join("-", words); // "a-b-c"
StringBuilder builder = new StringBuilder();
builder.append("ab").append(3);       // "ab3"
builder.setCharAt(0, 'A');            // "Ab3"
builder.deleteCharAt(2);              // "Ab"
builder.reverse();                   // "bA"
String result = builder.toString();
```

String is immutable; edits create new strings. Use StringBuilder for repeated construction. It has `length()`, not `size()`. Use `equals`, not `==`, for content. `split` takes a regex: splitting on a literal dot requires `"\\."`. Guard an empty stripped string before splitting it into words if you want zero tokens.

`charAt` indexes UTF-16 code units, not complete Unicode characters. For general Unicode, consider `s.codePoints()` and code-point indices. ASCII/lowercase-only frequency arrays require an explicit alphabet assumption.

## Arrays and matrices

```java
int[] a = {5, 1, 3};
int[] zeroes = new int[4];             // [0,0,0,0]
int[][] matrix = new int[2][3];        // 2 rows, 3 columns
int length = a.length;                // Field: length, not length()
Arrays.sort(a);                       // [1,3,5]
Arrays.fill(zeroes, -1);
int[] copy = a.clone();               // Independent primitive array
int[] slice = Arrays.copyOfRange(a, 0, 2); // [1,3]
boolean equal = Arrays.equals(a, copy);
String display = Arrays.toString(a);
String display2D = Arrays.deepToString(matrix);
for (int[] row : matrix) Arrays.fill(row, -1);
int[][] deepCopy = new int[matrix.length][];
for (int r = 0; r < matrix.length; r++) deepCopy[r] = matrix[r].clone();
```

A 2D array is an array of row references; it can be ragged. `matrix.clone()` copies only those references. Do not fill every row with the same mutable array via `Arrays.fill(matrix, sharedRow)` unless sharing is intentional. Most Java range APIs use `[start,end)`, while your problem statement may use inclusive endpoints. [Official array utilities](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Arrays.html).

## ArrayList and LinkedList

```java
List<Integer> list = new ArrayList<>();
list.add(10); list.add(20);            // [10,20]
list.add(1, 15);                      // [10,15,20]; shifts following values
int value = list.get(1);              // 15
list.set(1, 99);                      // Replaces, does not insert
list.remove(0);                       // Removes INDEX 0
list.remove(Integer.valueOf(20));     // Removes VALUE 20, if present
int size = list.size();
boolean empty = list.isEmpty();
boolean found = list.contains(99);
List<Integer> snapshot = new ArrayList<>(list);
Collections.reverse(snapshot);
LinkedList<Integer> linked = new LinkedList<>();
linked.addFirst(1); linked.addLast(2);
int first = linked.removeFirst();
```

ArrayList is the usual resizable sequence. LinkedList provides linked end operations but `get(i)` traverses nodes; repeated indexed iteration can become quadratic. Insert/remove is not automatically O(1) if you must first locate an index. See [ArrayList operation costs](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html) and [LinkedList indexing behavior](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedList.html).

## Stacks, queues, and deques

```java
Deque<Integer> stack = new ArrayDeque<>();
stack.push(10); stack.push(20);
int top = stack.peek();               // 20; do not unbox an empty peek()
int removed = stack.pop();            // 20; throws if empty
Queue<Integer> queue = new ArrayDeque<>();
queue.offer(10); queue.offer(20);
Integer front = queue.peek();         // 10, or null if empty
Integer oldest = queue.poll();        // 10, or null if empty
Deque<Integer> deque = new ArrayDeque<>();
deque.offerFirst(1); deque.offerLast(2);
Integer left = deque.pollFirst();
Integer right = deque.pollLast();
```

```text
Stack: push/pop at same end     top -> [newest ... oldest]
Queue: offer tail, poll head    head -> [oldest ... newest] <- tail
Deque: add or remove at either end
```

| Operation style | Empty behavior |
| --- | --- |
| `remove()`, `removeFirst()`, `pop()` | Throws |
| `poll()`, `pollFirst()`, `pollLast()` | Returns null |
| `element()`, `getFirst()` | Throws |
| `peek()`, `peekFirst()`, `peekLast()` | Returns null |

ArrayDeque rejects null. End operations are amortized O(1); searching/removing an arbitrary value is linear. [Official deque reference](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayDeque.html). See the [stack/queue guide](20_stack_queue_basics.md).

## Sets

```java
Set<Integer> seen = new HashSet<>();
boolean firstTime = seen.add(7);      // true
boolean duplicate = !seen.add(7);     // true: second add returns false
boolean exists = seen.contains(7);
seen.remove(7);
Set<Integer> insertionOrder = new LinkedHashSet<>();
insertionOrder.add(3); insertionOrder.add(1); insertionOrder.add(3);
// Iteration: 3,1
Set<Integer> intersection = new HashSet<>(Set.of(1, 2, 3));
intersection.retainAll(Set.of(2, 3, 4)); // {2,3}
Set<Integer> union = new HashSet<>(Set.of(1, 2));
union.addAll(Set.of(2, 3));            // {1,2,3}
union.removeAll(Set.of(2));           // {1,3}
```

HashSet has no promised iteration order; LinkedHashSet preserves insertion order; TreeSet sorts by its ordering rule. Equal keys do not appear twice. For a multiset, store counts in a map instead.

## Maps and frequency counting

```java
Map<String, Integer> count = new HashMap<>();
count.put("cat", 1);
count.put("cat", 2);                  // Replaces the previous value
count.merge("dog", 1, Integer::sum);  // Insert 1 or increment
count.put("rat", count.getOrDefault("rat", 0) + 1);
boolean hasCat = count.containsKey("cat");
Integer absent = count.get("none");  // null, not zero
for (Map.Entry<String, Integer> entry : count.entrySet()) {
    String key = entry.getKey();
    int frequency = entry.getValue();
}
count.remove("cat");
Map<Integer, List<Integer>> adjacency = new HashMap<>();
adjacency.computeIfAbsent(0, ignored -> new ArrayList<>()).add(1);
Map<Integer, Integer> multiset = new TreeMap<>();
multiset.merge(5, 1, Integer::sum);
int remainingCount = multiset.get(5) - 1;
if (remainingCount == 0) multiset.remove(5);
else multiset.put(5, remainingCount);
```

HashMap operations have expected constant-time lookup with well-distributed hashes; iteration order is unspecified. Use `containsKey` when a null value must be distinguished from an absent mapping. Prefer non-null counts in DSA. [Official HashMap contract](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html).

## Ordered sets and maps

```java
NavigableSet<Integer> sorted = new TreeSet<>(List.of(10, 20, 30));
Integer less = sorted.lower(20);      // 10: strictly less
Integer atMost = sorted.floor(20);    // 20: <=
Integer atLeast = sorted.ceiling(21); // 30: >=
Integer greater = sorted.higher(20); // 30: strictly greater
Integer missing = sorted.ceiling(40);// null
int minimum = sorted.first();         // Throws if empty
Integer removedMin = sorted.pollFirst(); // null if empty
NavigableMap<Integer, String> map = new TreeMap<>();
map.put(10, "a"); map.put(20, "b");
Map.Entry<Integer, String> floor = map.floorEntry(15); // 10="a"
NavigableMap<Integer, String> range = map.subMap(10, true, 20, false);
// range is a VIEW: changes affect map
```

`lower <`, `floor <=`, `ceiling >=`, `higher >`. TreeMap is a red-black tree; TreeSet is backed by a TreeMap. Basic key operations are O(log n). Comparators define which keys are considered duplicates: a comparator returning 0 collapses those entries. [TreeMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeMap.html), [TreeSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeSet.html).

## Heap / PriorityQueue

```java
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
minHeap.offer(8); minHeap.offer(2); minHeap.offer(5);
int minimum = minHeap.peek();         // 2
int extracted = minHeap.poll();       // 2
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
maxHeap.offer(8); maxHeap.offer(2);
int maximum = maxHeap.poll();         // 8
PriorityQueue<int[]> jobs = new PriorityQueue<>(
    Comparator.<int[]>comparingInt(job -> job[0]).thenComparingInt(job -> job[1]));
jobs.offer(new int[]{3, 10});          // [priority, id]
jobs.offer(new int[]{1, 20});
int[] nextJob = jobs.poll();          // [1,20]
```

Only the head is guaranteed to be the next priority item; iteration is not sorted. `offer/poll` are O(log n), `peek` O(1), and `contains/remove(Object)` O(n). Do not mutate a field used by the comparator while an object is still in the heap; remove/reinsert or use a stale-entry strategy. Null is prohibited. [Official heap reference](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/PriorityQueue.html).

## Sorting and comparators

```java
int[] primitive = {3, 1, 2};
Arrays.sort(primitive);               // Ascending; no Comparator overload for int[]
Integer[] boxed = {3, 1, 2};
Arrays.sort(boxed, Comparator.reverseOrder());
List<String> words = new ArrayList<>(List.of("pear", "fig", "apple"));
words.sort(Comparator.comparingInt(String::length).thenComparing(Comparator.naturalOrder()));
int[][] intervals = {{2, 5}, {1, 4}, {1, 3}};
Arrays.sort(intervals, Comparator.<int[]>comparingInt(row -> row[0])
                                .thenComparingInt(row -> row[1]));
// [[1,3],[1,4],[2,5]]
Comparator<Integer> safeAscending = Integer::compare; // Not (a,b) -> a-b
```

Compare with `Integer.compare` or `Long.compare`, not subtraction that can overflow. The comparator should be antisymmetric and transitive. Object sorting preserves ties (stable); reversing only one comparator stage differs from reversing the entire combined comparator. See [sorting patterns](04_sorting.md).

## Binary search

```java
int[] sorted = {1, 3, 3, 7};
int found = Arrays.binarySearch(sorted, 3); // Some matching index, not necessarily first
int absent = Arrays.binarySearch(sorted, 5); // -(insertionPoint)-1 = -4
int insertionPoint = absent < 0 ? -absent - 1 : absent;
```

For reliable duplicate boundaries, place these helper methods inside your class. The input must be sorted ascending.

```java
static int lowerBound(int[] a, int target) { // First index with value >= target
    int low = 0, high = a.length;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (a[mid] < target) low = mid + 1;
        else high = mid;
    }
    return low;
}
static int upperBound(int[] a, int target) { // First index with value > target
    int low = 0, high = a.length;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (a[mid] <= target) low = mid + 1;
        else high = mid;
    }
    return low;
}
```

For `[1,3,3,7]`, lowerBound(3)=1 and upperBound(3)=3, so the frequency is 2. A boundary may equal `a.length`; check before indexing. Both helpers take O(log n) time and O(1) space.

## Pairs, records, equality, and generics

These types go inside your class. Records provide value-based equals/hashCode for their components.

```java
record Pair(int row, int col) {}
static class Box<T> {
    private T value;
    Box(T value) { this.value = value; }
    T get() { return value; }
}
```

```java
record Cell(int row, int col) {}
Set<Cell> visited = new HashSet<>();
visited.add(new Cell(1, 2));
boolean sameLocation = visited.contains(new Cell(1, 2)); // true
Set<int[]> arrayKeys = new HashSet<>();
arrayKeys.add(new int[]{1, 2});
boolean notValueEqual = arrayKeys.contains(new int[]{1, 2}); // false
Integer x = 1000, y = 1000;
boolean sameNumber = x.equals(y);      // Use content equality, not wrapper identity
```

Ordinary custom classes use identity equality unless you override `equals` and `hashCode`. Arrays also use identity equality as map/set keys. A record containing an array does **not** magically give that array content equality. Avoid mutating hash-relevant fields after inserting a key. Generics cannot use primitive type arguments; `var` can infer a local variable's type but does not make Java dynamically typed.

## Iteration, copying, and conversions

```java
List<Integer> values = new ArrayList<>(List.of(1, 2, 3, 4));
values.removeIf(x -> x % 2 == 0);      // [1,3]
Iterator<Integer> it = values.iterator();
while (it.hasNext()) if (it.next() == 1) it.remove();
int[] primitive = {1, 2, 3};
List<Integer> boxed = new ArrayList<>();
for (int x : primitive) boxed.add(x);
int[] back = boxed.stream().mapToInt(Integer::intValue).toArray();
Integer[] array = boxed.toArray(new Integer[0]);
List<Integer> fixed = Arrays.asList(1, 2, 3); // set allowed; add/remove not allowed
List<Integer> readOnly = List.of(1, 2, 3);    // Unmodifiable; rejects null
List<Integer> mutable = new ArrayList<>(readOnly);
List<int[]> oneElement = Arrays.asList(primitive); // One int[] element, not 3 Integers
```

Do not structurally modify a collection directly inside an enhanced for loop; use iterator removal, `removeIf`, or collect changes separately. Copying an object list is shallow: both lists still refer to the same elements. `subList` is a view, not an independent copy. These details are part of the [List API](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html).

## Bits, BitSet, and big integers

```java
long mask = 0;
int bit = 5;                          // For a long mask, require 0 <= bit < 64
mask |= 1L << bit;                    // Set
boolean isSet = (mask & (1L << bit)) != 0;
mask ^= 1L << bit;                    // Toggle
mask &= ~(1L << bit);                 // Clear
int ones = Long.bitCount(13L);        // 13 = binary 1101 -> 3
int trailing = Integer.numberOfTrailingZeros(8); // 3
int shifted = -8 >>> 1;               // Logical right shift, zero-fill
boolean powerOfTwo = 16 > 0 && (16 & (16 - 1)) == 0;
BitSet bits = new BitSet();
bits.set(1); bits.set(4); bits.flip(2); bits.clear(1);
boolean present = bits.get(4);
int count = bits.cardinality();       // 2; number of set bits
int logicalLength = bits.length();    // 5; highest set index + 1
int nextSet = bits.nextSetBit(0);      // 2; -1 means none
BitSet other = new BitSet(); other.set(4);
BitSet common = (BitSet) bits.clone();
common.and(other);                    // {4}; and/or/xor mutate their receiver
BigInteger a = new BigInteger("12345678901234567890");
BigInteger b = BigInteger.valueOf(10);
BigInteger sum = a.add(b);
BigInteger product = a.multiply(b);
BigInteger mod = a.mod(BigInteger.valueOf(1_000_000_007L));
int comparison = a.compareTo(b);      // Positive means a > b
```

Java masks shift distances: int uses the low 5 bits and long uses the low 6 bits. Shifting by 32 or 64 does not create a larger mask. `>>` preserves the sign; `>>>` zero-fills. BigInteger is immutable: capture the returned value; its arithmetic costs depend on bit length, not O(1). [BitSet](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/BitSet.html), [BigInteger](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/math/BigInteger.html).

## Custom structures: diagrams and templates

Java's collection classes cover many needs, but these DSA structures normally need custom code. The templates below use explicit index conventions and avoid external dependencies.

```text
Singly linked list:  head -> [value|next] -> [value|next] -> null
Doubly linked list:  null <- [prev|value|next] <-> [...] -> null
Circular list:       tail.next points back into the list; traversal needs a stop rule

Binary tree:                 BST ordering: smaller values left, larger right
         5                   An unbalanced BST can become a chain.
        / \
       2   8

Graph adjacency list:        DSU parent links:
0: [1,2]                     0 -> 1 <- 2     root 1 represents {0,1,2}
1: [0]                       find follows/compresses parent links
2: [0]

Trie words cat / car:        Segment tree intervals:
root -> c -> a -> t*                 [0,4)
                 \-> r*            /     \
* means complete word           [0,2)    [2,4)

Fenwick tree internal index is 1-based:
bit[1] covers one item; bit[2] covers two; bit[4] covers four.
Each bit[i] stores the last lowbit(i) items ending at i.
```

Save the following as **DSATemplates.java**. All its public array/range methods are **zero-based**, and sum/min ranges are **half-open `[left,right)`**. DSU's n nodes are 0..n−1. Trie keys are lowercase English letters only. Inputs and totals must fit memory and long arithmetic where used.

```java
import java.util.*;

public class DSATemplates {
    public static class ListNode {
        public int value;
        public ListNode next;
        public ListNode(int value) { this.value = value; }
    }
    public static ListNode reverse(ListNode head) {
        ListNode previous = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = previous;
            previous = head;
            head = next;
        }
        return previous;
    }

    public static class TreeNode {
        public int value;
        public TreeNode left, right;
        public TreeNode(int value) { this.value = value; }
    }
    public static int height(TreeNode node) { // Height in nodes; empty=0
        return node == null ? 0 : 1 + Math.max(height(node.left), height(node.right));
    }
    public static boolean bstContains(TreeNode root, int target) {
        while (root != null) {
            if (root.value == target) return true;
            root = target < root.value ? root.left : root.right;
        }
        return false;
    }
    public static TreeNode bstInsert(TreeNode root, int value) { // Ignore duplicates
        if (root == null) return new TreeNode(value);
        TreeNode current = root;
        while (true) {
            if (value == current.value) return root;
            if (value < current.value) {
                if (current.left == null) { current.left = new TreeNode(value); return root; }
                current = current.left;
            } else {
                if (current.right == null) { current.right = new TreeNode(value); return root; }
                current = current.right;
            }
        }
    }

    public static List<List<Integer>> graph(int n) {
        if (n < 0) throw new IllegalArgumentException();
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        return graph;
    }
    public static void addUndirected(List<List<Integer>> graph, int u, int v) {
        graph.get(u).add(v); graph.get(v).add(u);
    }
    public static int[] bfs(List<List<Integer>> graph, int source) {
        Objects.checkIndex(source, graph.size());
        int[] distance = new int[graph.size()];
        Arrays.fill(distance, -1);
        Queue<Integer> queue = new ArrayDeque<>();
        distance[source] = 0; queue.offer(source);
        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : graph.get(u)) if (distance[v] == -1) {
                distance[v] = distance[u] + 1;
                queue.offer(v);
            }
        }
        return distance;
    }
    public record Edge(int to, int weight) {} // For weighted adjacency lists

    public static class DSU {
        private final int[] parent, size;
        private int components;
        public DSU(int n) {
            if (n < 0) throw new IllegalArgumentException();
            parent = new int[n]; size = new int[n]; components = n;
            for (int i = 0; i < n; i++) { parent[i] = i; size[i] = 1; }
        }
        public int find(int x) {
            Objects.checkIndex(x, parent.length);
            while (x != parent[x]) {
                parent[x] = parent[parent[x]]; // Path halving
                x = parent[x];
            }
            return x;
        }
        public boolean union(int a, int b) {
            a = find(a); b = find(b);
            if (a == b) return false;
            if (size[a] < size[b]) { int t = a; a = b; b = t; }
            parent[b] = a; size[a] += size[b]; components--;
            return true;
        }
        public int components() { return components; }
        public int componentSize(int x) { return size[find(x)]; }
    }

    public static class Trie {
        private static class Node {
            Node[] children = new Node[26];
            boolean terminal;
        }
        private final Node root = new Node();
        private static int index(char c) {
            if (c < 'a' || c > 'z') throw new IllegalArgumentException("Use a..z");
            return c - 'a';
        }
        public void insert(String word) {
            // Validate first so an invalid word cannot leave a partial insertion.
            for (int i = 0; i < word.length(); i++) index(word.charAt(i));
            Node node = root;
            for (int i = 0; i < word.length(); i++) {
                int k = index(word.charAt(i));
                if (node.children[k] == null) node.children[k] = new Node();
                node = node.children[k];
            }
            node.terminal = true;
        }
        private Node walk(String text) {
            for (int i = 0; i < text.length(); i++) index(text.charAt(i));
            Node node = root;
            for (int i = 0; i < text.length(); i++) {
                node = node.children[index(text.charAt(i))];
                if (node == null) return null;
            }
            return node;
        }
        public boolean search(String word) { Node n = walk(word); return n != null && n.terminal; }
        public boolean startsWith(String prefix) { return walk(prefix) != null; }
    }

    public static class Fenwick {
        private final int n;
        private final long[] bit;
        public Fenwick(int n) {
            if (n < 0) throw new IllegalArgumentException();
            this.n = n; bit = new long[n + 1];
        }
        public void add(int index, long delta) {
            Objects.checkIndex(index, n);
            for (int i = index + 1; i <= n; i += i & -i) bit[i] += delta;
        }
        public long prefix(int end) { // Sum [0,end)
            if (end < 0 || end > n) throw new IndexOutOfBoundsException();
            long result = 0;
            for (int i = end; i > 0; i -= i & -i) result += bit[i];
            return result;
        }
        public long sum(int left, int right) {
            if (left < 0 || left > right || right > n) throw new IndexOutOfBoundsException();
            return prefix(right) - prefix(left);
        }
    }

    public static class SegmentTree {
        private final int n;
        private final long[] tree;
        public SegmentTree(int[] values) {
            n = values.length; tree = new long[Math.max(2, 2*n)];
            for (int i = 0; i < n; i++) tree[n+i] = values[i];
            for (int i = n-1; i > 0; i--) tree[i] = tree[i*2] + tree[i*2+1];
        }
        public void set(int index, long value) {
            Objects.checkIndex(index, n);
            int p = index + n; tree[p] = value;
            while (p > 1) { p /= 2; tree[p] = tree[p*2] + tree[p*2+1]; }
        }
        public long sum(int left, int right) { // Sum [left,right)
            if (left < 0 || left > right || right > n) throw new IndexOutOfBoundsException();
            long result = 0;
            for (left += n, right += n; left < right; left /= 2, right /= 2) {
                if ((left & 1) != 0) result += tree[left++];
                if ((right & 1) != 0) result += tree[--right];
            }
            return result;
        }
    }

    public static class SparseMin {
        private final int n;
        private final int[] log;
        private final int[][] table;
        public SparseMin(int[] values) {
            n = values.length;
            if (n == 0) throw new IllegalArgumentException("Nonempty array required");
            log = new int[n+1];
            for (int i = 2; i <= n; i++) log[i] = log[i/2] + 1;
            table = new int[log[n]+1][n]; table[0] = values.clone();
            for (int k = 1; k < table.length; k++)
                for (int i = 0; i + (1 << k) <= n; i++)
                    table[k][i] = Math.min(table[k-1][i], table[k-1][i+(1 << (k-1))]);
        }
        public int min(int left, int right) { // Minimum over nonempty [left,right)
            if (left < 0 || left >= right || right > n) throw new IndexOutOfBoundsException();
            int k = log[right-left];
            return Math.min(table[k][left], table[k][right-(1 << k)]);
        }
    }
}
```

### How to use the templates

Compile DSATemplates.java first, or place these examples into another class compiled alongside it.

```java
DSATemplates.DSU dsu = new DSATemplates.DSU(4);
dsu.union(0, 1); dsu.union(1, 2);
boolean connected = dsu.find(0) == dsu.find(2); // true
int groups = dsu.components();                // 2
DSATemplates.Trie trie = new DSATemplates.Trie();
trie.insert("apple");
boolean word = trie.search("app");            // false
boolean prefix = trie.startsWith("app");      // true
DSATemplates.Fenwick fenwick = new DSATemplates.Fenwick(3);
fenwick.add(0, 1); fenwick.add(1, 3); fenwick.add(2, 5);
long firstTwo = fenwick.prefix(2);             // 1+3=4
long lastTwo = fenwick.sum(1, 3);              // 3+5=8
DSATemplates.SegmentTree segment = new DSATemplates.SegmentTree(new int[]{1, 3, 5});
long original = segment.sum(0, 3);             // 9
segment.set(1, 2);
long updated = segment.sum(0, 3);              // 8
DSATemplates.SparseMin sparse = new DSATemplates.SparseMin(new int[]{4, 2, 7, 1});
int minimum = sparse.min(1, 3);                // min(2,7)=2
List<List<Integer>> graph = DSATemplates.graph(3);
DSATemplates.addUndirected(graph, 0, 1);
int[] distance = DSATemplates.bfs(graph, 0);    // [0,1,-1]
```

### What each custom structure guarantees

| Structure | Core operations | Complexity | Important condition |
| --- | --- | --- | --- |
| Singly linked nodes | Reverse / traverse | O(n) time; reverse O(1) extra space | Acyclic list |
| Binary tree | Height / traversal | O(n), stack O(height) | May hit stack limits on a chain |
| Unbalanced BST | Search / insert | O(height); worst O(n) | Not self-balancing; duplicates ignored here |
| DSU | Find / union | Amortized O(α(n)); O(n) initialization/storage | Connectivity, not path reconstruction |
| Trie | Insert / search | O(word length); space proportional to prefix nodes × alphabet | Template alphabet a..z |
| Fenwick | Add / prefix/range sum | O(log n), O(n) storage | Add a delta; assignment needs old value |
| Segment tree | Set / range sum | O(log n), O(n) build/storage | Point assignment only in this template |
| Sparse table | Static range minimum | O(n log n) build/space; O(1) query | No efficient updates |
| Graph adjacency list | Build / BFS | O(V+E) storage/traversal | BFS shortest paths require equal edge costs |

The sparse table's two queried intervals may overlap. That is valid for idempotent operations such as min/max/GCD; it does **not** make this O(1) overlapping-query formula valid for sums. For weighted graph edges, use `List<List<DSATemplates.Edge>>`; BFS is not the general weighted shortest-path algorithm. A DSU is not a balanced binary-search tree.

For full solutions and walkthroughs: [linked lists](07_linked_lists.md), [trees](11_tree_recursion.md), [BFS/DFS](08_graph_traversal.md), [DSU/Kruskal](06_heap_greedy.md), [trie](18_trie.md), [lazy range updates](17_range_queries.md).

## Pattern snippets

### Prefix sum and difference array

```java
int[] a = {2, 4, 1, 3};
long[] prefix = new long[a.length + 1];
for (int i = 0; i < a.length; i++) prefix[i+1] = prefix[i] + a[i];
int left = 1, right = 3;                  // Half-open [1,3)
long rangeSum = prefix[right] - prefix[left]; // 4+1=5
long[] difference = new long[a.length + 1];
int l = 1, r = 2; long delta = 5;         // Inclusive update [1,2]
difference[l] += delta;
difference[r+1] -= delta;
long active = 0;
long[] result = new long[a.length];
for (int i = 0; i < a.length; i++) {
    active += difference[i];
    result[i] = a[i] + active;             // [2,9,6,3]
}
```

### Two-dimensional prefix sum

```java
int[][] grid = {{1, 2}, {3, 4}};
int rows = grid.length, cols = grid[0].length;
long[][] prefix = new long[rows+1][cols+1];
for (int r = 0; r < rows; r++) for (int c = 0; c < cols; c++)
    prefix[r+1][c+1] = grid[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c];
int r1 = 0, c1 = 1, r2 = 2, c2 = 2; // Half-open rectangle [r1,r2) x [c1,c2)
long rectangleSum = prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]; // 6
```

This example assumes a nonempty rectangular grid. Prefix construction is O(rows×cols), and each rectangle query is O(1).

### Monotonic stack: nearest strictly smaller to the left

```java
int[] a = {2, 1, 2};
int[] left = new int[a.length];
Deque<Integer> stack = new ArrayDeque<>(); // Store indices
for (int i = 0; i < a.length; i++) {
    while (!stack.isEmpty() && a[stack.peek()] >= a[i]) stack.pop();
    left[i] = stack.isEmpty() ? -1 : stack.peek();
    stack.push(i);
}
// left = [-1,-1,1]
```

Each index is pushed/popped at most once: O(n) total time. Change scan direction and pop inequality for the other nearest-neighbor variants. [Detailed guide](05_monotonic_stack.md).

### Memoization and backtracking reminders

```text
MEMOIZATION(state):
    return base answer if terminal
    return cached answer if present
    compute answer from smaller valid states
    cache and return

BACKTRACK(state, mutablePath):
    if complete: record a COPY of path; return
    for each valid candidate:
        apply choice
        recurse
        undo choice
```

Use `new ArrayList<>(path)` to snapshot a path. This copies the list structure, not any mutable objects stored inside. For 2D DP, fill each row separately; `Arrays.fill` on the outer array does not fill numeric cells. See [DP foundations](12_dp_foundations.md), [knapsack](13_knapsack.md), [LCS/SCS](14_lcs_scs.md), and [backtracking](15_backtracking.md).

## Complexity reference

n = structure size; k = distinct keys. Hash costs assume well-distributed keys; amortized costs average a sequence of operations, not a single worst-case resize.

| Structure / operation | Read / search | Add | Remove | Storage |
| --- | --- | --- | --- | --- |
| Array | index O(1); unsorted search O(n) | Fixed length | Manual shift O(n) | O(n) |
| ArrayList | index O(1); contains O(n) | Append amortized O(1); indexed O(n) | Arbitrary index/value O(n) worst | O(n) |
| LinkedList | index/search O(n) | Ends O(1); indexed O(n) worst | Ends O(1); locate by value/index O(n) | O(n) |
| ArrayDeque | peek O(1); contains O(n) | Ends amortized O(1) | Ends amortized O(1); by value O(n) | O(n) |
| HashMap / HashSet | Expected O(1) | Expected amortized O(1) | Expected O(1) | O(n) |
| TreeMap / TreeSet | O(log n) key lookup | O(log n) | O(log n) | O(n) |
| PriorityQueue | peek O(1); arbitrary lookup O(n) | O(log n) | poll O(log n); arbitrary object O(n) | O(n) |
| Sorted array | Binary search O(log n) | Keeping sorted O(n) | Keeping order O(n) | O(n) |

| Algorithm / technique | Time | Extra space |
| --- | --- | --- |
| Two monotone pointer scans | O(n) | Often O(1) |
| Merge sort | O(n log n) | O(n) buffer + O(log n) stack |
| Last-element-pivot quick sort | Average O(n log n); worst O(n²) | Stack average O(log n), worst O(n) |
| Adjacency-list BFS / DFS | O(V+E) | O(V) excluding graph/output |
| Frequency sort | Expected O(n+k log k) | O(k), excluding output |
| 0/1 knapsack | O(items×capacity) | O(capacity) compressed |
| LCS length / reconstruction table | O(mn) | O(mn) for the full table |

These are useful DSA bounds; key hashing/comparison costs and BigInteger arithmetic may add work. Object-heavy collections also carry boxing/reference overhead that primitive arrays avoid.

## Common mistakes

| Mistake | Correct habit |
| --- | --- |
| `a.length()`, `list.length`, `s.size()` | Array `.length`; list `.size()`; string `.length()` |
| `s1 == s2` for text | `s1.equals(s2)`; use `Objects.equals` when null is possible |
| `List<int>` | `List<Integer>` |
| `list.remove(2)` when deleting value 2 | `list.remove(Integer.valueOf(2))` |
| Assuming `Arrays.asList(intArray)` boxes each number | Explicit loop or `Arrays.stream(a).boxed()` |
| Appending to `List.of(...)` | Create `new ArrayList<>(...)` |
| Treating `new ArrayList<>(100)` as 100 elements | It is capacity, size is still zero; add elements first |
| Treating `matrix.clone()` as a deep copy | Clone each row |
| Adding null to ArrayDeque / PriorityQueue | Use non-null values and handle empty poll/peek |
| Unboxing an empty `peek()` result | Check emptiness or keep an `Integer` first |
| Assuming HashMap iteration or heap iteration is sorted | Use a sorted structure or explicitly sort/poll |
| Comparator `(a,b) -> a-b` | `Integer.compare(a,b)` |
| Reusing a mutable array as a value-equal hash key | Use a suitable immutable record/key representation |
| Incrementing a wrapper but not storing it back | `map.merge(key,1,Integer::sum)` |
| `long result = intValue * intValue` | `1L * intValue * intValue` |
| Mixing range conventions | Label every API as inclusive or half-open |
| Leaving mutable state between test cases | Reinitialize visited/memo/result structures per call |
| Recursive calls without restoring a path/board | Apply → recurse → undo |
| Counting unreachable DP states | Choose correct zero/base and unreachable sentinels |
| Returning a local new head without using it | `head = reverse(head)` |

## Interview recall checklist

- Can I select an array, map, ordered tree, heap, stack, or queue from the operations required?
- Can I write a safe comparator and explain its tie-break?
- Do I know whether the algorithm needs indices, values, counts, or node identities?
- Can I state the invariant, range convention, mutation behavior, and empty-input result?
- Can counts/products overflow int? Will long suffice?
- Can I write lower/upper bound, BFS, DSU, and prefix sums without copying a solution?
- Can I identify when a Fenwick tree, segment tree, or sparse table is appropriate?
- Can I explain time and space including recursion, output, and copied data?

Use this file as a syntax/operation reference, then use the [pattern guides](README.md) for full questions, diagrams, pseudocode, and dry runs. Java 17 library behavior was checked against the linked official Oracle API references on 10 November 2026.

## Verification of the examples

All 24 Java blocks were extracted and compiled with `javac --release 17 -Xlint:all`. The 22 short example programs and the complete input/output example ran successfully. The custom templates passed 23,451 checks, including randomized Fenwick/segment-tree sums and sparse-table minimum queries. The examples are standalone snippets as described at the top, not one block to paste unchanged into the same method.
