Perfect — everything selected, which means we start from absolute zero. That's actually the best place to start because we'll build it the right way without any bad habits.

Here's the exact path we'll follow:

**Recursion → Memoization → Tabulation → Space optimization**

We won't touch DP until recursion clicks. Let's go.

---

## Stage 1 — Recursion: the foundation of everything

Before DP, you need one core belief:

> **Any problem that can be broken into smaller versions of itself can be solved with recursion.**

### The 3-part mental model for every recursive function

```
1. Base case   → When do I stop?
2. Hypothesis  → Assume the function works correctly for smaller input
3. Induction   → Use that result to solve the current input
```

This is called the **IBH method** (Induction-Base-Hypothesis) and it's the cleanest way to think about recursion. Let's apply it to the simplest possible problem.

---

### Problem 1 — Print numbers from N down to 1

```python
def countdown(n):
    # BASE CASE: when do we stop?
    if n == 0:
        return

    # CURRENT WORK: do something at this level
    print(n)

    # INDUCTION: trust that countdown(n-1) handles the rest
    countdown(n - 1)

countdown(5)
# Output: 5 4 3 2 1
```

Notice the structure — you only think about **one level**. You do your job (`print n`), then hand the rest to a smaller version of yourself.

---

### Problem 2 — Factorial

```python
def factorial(n):
    # BASE CASE
    if n == 0:
        return 1          # 0! = 1 by definition

    # HYPOTHESIS: assume factorial(n-1) gives (n-1)! correctly
    # INDUCTION: use it
    return n * factorial(n - 1)
```

Call stack for `factorial(4)`:

```
factorial(4)
└── 4 * factorial(3)
        └── 3 * factorial(2)
                └── 2 * factorial(1)
                        └── 1 * factorial(0)
                                └── returns 1
                        returns 1
                returns 2
        returns 6
returns 24
```

The key thing to observe — **each call waits** for the one below it to finish before it can compute its own answer. This waiting chain is what the **call stack** is. Every recursive call adds a frame to it.

---

### Problem 3 — Fibonacci (where DP will matter later)

```python
def fib(n):
    # BASE CASES
    if n == 0: return 0
    if n == 1: return 1

    # fib(n) = fib(n-1) + fib(n-2)
    return fib(n - 1) + fib(n - 2)
```

This one branches — each call spawns **two** more calls. Draw the tree for `fib(5)`:

```
                     fib(5)
                   /        \
               fib(4)        fib(3)
              /      \       /     \
          fib(3)  fib(2) fib(2)  fib(1)
          /    \
       fib(2) fib(1)
```

Notice something? **`fib(3)` is computed twice. `fib(2)` is computed three times.** This is the exact problem DP solves — but we'll get there. For now just observe it.

Time complexity of this naive recursion: **O(2ⁿ)** — doubles with every input. Terrible. For `fib(50)` that's over a trillion calls.

---

### The call stack — why recursion can be slow or crash

Every function call in Python uses memory on the call stack. Recursion with depth `n` uses `O(n)` stack space. Python's default limit is ~1000 calls deep — go beyond that and you get:

```
RecursionError: maximum recursion depth exceeded
```

This is why iterative solutions or memoization (which avoids redundant calls) are preferred for large inputs.

---

### How to think about any recursive problem — the 3 questions

Before writing a single line of code, answer these:

```
1. What does my function return/do?
   → Define it precisely in English first

2. What is the smallest input where I know the answer directly?
   → That's your base case

3. If I had the answer for (n-1), how do I get the answer for n?
   → That's your recursive step
```

For `fib(n)`:

1. "Returns the nth Fibonacci number"
2. "fib(0) = 0, fib(1) = 1" — I know these directly
3. "fib(n) = fib(n-1) + fib(n-2)"

---

### Quick practice — try this mentally before reading the answer

**Question:** Write a recursive function `sum_array(arr, n)` that returns the sum of the first `n` elements of an array.

Think through the 3 questions:

1. What does it return? → Sum of first n elements
2. Base case? → When n is 0, sum is 0
3. Recursive step? → `arr[n-1] + sum_array(arr, n-1)`

```python
def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sum_array(arr, n - 1)
```

---

## What's coming next

Once this recursion foundation is solid, the jump to DP is actually small — just one key observation:

> **DP = Recursion + "Don't solve the same subproblem twice"**

The Fibonacci tree you saw above? DP fixes exactly that — `fib(3)` gets computed once and remembered. That's memoization, and it's Stage 2.

---

**Before we move to Stage 2, one question for you:**

Look at this function:

```python
def mystery(n):
    if n == 1:
        return 0
    return 1 + mystery(n // 2)
```

What does `mystery(8)` return, and what does this function compute? Trace it step by step and tell me your answer — don't run it, think through it. This will confirm whether the base case + induction model has clicked.


Exactly right! Let's verify your trace:

```
mystery(8)
└── 1 + mystery(4)
        └── 1 + mystery(2)
                └── 1 + mystery(1)
                        └── returns 0

# Unwinding back up:
mystery(1) = 0
mystery(2) = 1 + 0 = 1
mystery(4) = 1 + 1 = 2
mystery(8) = 1 + 2 = 3  ✓
```

And did you notice **what it computes?** Every call divides `n` by 2 and adds 1 — it's counting **how many times you can halve n before reaching 1**. That's `log₂(n)`. So `mystery(n)` = **log₂(n)**.

This is actually important — whenever you see a recursion that halves its input, its time complexity is O(log n). Binary search works the same way.

Recursion is clicking. Let's move to Stage 2.

---

## Stage 2 — Memoization: fixing the redundant work

Remember the Fibonacci tree where `fib(3)` was computed twice and `fib(2)` three times? Let's quantify how bad that gets:

```
fib(5)  →  15 calls
fib(10) →  177 calls
fib(20) →  21,891 calls
fib(50) →  ~2 trillion calls  ← your computer dies here
```

The fix is embarrassingly simple:

> **Before computing, check if you've already solved this. If yes, return the stored answer. If no, compute it, store it, then return it.**

This is **memoization** — memo as in "note to self", not memorization.

---

### Fibonacci with memoization

```python
from functools import cache

@cache
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)
```

That's literally it. `@cache` is Python doing the storing for you. But let's do it manually so you understand what's happening inside:

```python
def fib(n, memo={}):
    # Check: have I solved this before?
    if n in memo:
        return memo[n]       # return stored answer instantly

    # Base cases
    if n == 0: return 0
    if n == 1: return 1

    # Compute, STORE, then return
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

Now look at what the call tree becomes for `fib(5)`:

```
WITHOUT memo                    WITH memo
fib(5)                          fib(5)
├── fib(4)                      ├── fib(4)
│   ├── fib(3)                  │   ├── fib(3)
│   │   ├── fib(2)              │   │   ├── fib(2)
│   │   │   ├── fib(1)=1        │   │   │   ├── fib(1)=1
│   │   │   └── fib(0)=0        │   │   │   └── fib(0)=0
│   │   └── fib(1)=1            │   │   └── fib(1)=1 ✓ cached
│   └── fib(2) ← recomputed     │   └── fib(2) ✓ cached
│       ├── fib(1)=1            └── fib(3) ✓ cached
│       └── fib(0)=0
└── fib(3) ← recomputed again
    └── ... (all recomputed)

Total: 15 calls                 Total: 9 calls (each n solved once)
```

Every unique subproblem is solved **exactly once**. Since there are only `n` unique values of `fib` (from 0 to n), complexity drops from O(2ⁿ) to **O(n)**.

---

### The memoization template — works for almost every DP problem

```python
memo = {}

def solve(params):
    # 1. Base case
    if base_condition:
        return base_value

    # 2. Check cache
    if params in memo:
        return memo[params]

    # 3. Compute
    result = ... # recursive calls

    # 4. Store and return
    memo[params] = result
    return result
```

This 4-step template is all memoization ever is. The only thing that changes problem to problem is what `params` are and how you compute `result`.

---

### Now a real problem — Climbing Stairs (LC #70)

**Problem:** You can climb 1 or 2 steps at a time. How many distinct ways to reach step `n`?

**Apply the 3 questions:**

```
1. What does solve(n) return?
   → Number of distinct ways to reach step n

2. Base cases?
   → solve(0) = 1  (you're already there — one way: do nothing)
   → solve(1) = 1  (only one way: take 1 step)

3. Recursive step?
   → To reach step n, your last step was either from n-1 (took 1 step)
     or from n-2 (took 2 steps)
   → solve(n) = solve(n-1) + solve(n-2)
```

Looks familiar? It's Fibonacci in disguise.

```python
from functools import cache

def climbStairs(n):
    @cache
    def solve(i):
        if i == 0: return 1   # base: reached top
        if i == 1: return 1   # base: one way
        return solve(i-1) + solve(i-2)

    return solve(n)
```

Trace for `n = 4`:

```
solve(4) = solve(3) + solve(2)
solve(3) = solve(2) + solve(1)
solve(2) = solve(1) + solve(0) = 1 + 1 = 2  ← stored
solve(1) = 1
solve(3) = 2 + 1 = 3                         ← stored
solve(2) = 2                                  ← returned from cache!
solve(4) = 3 + 2 = 5
```

5 ways to climb 4 stairs. Verify: `{1111, 112, 121, 211, 22}` ✓

---

### Why `@cache` specifically?

You saw it in the `predictTheWinner` code and now here. Here's a precise breakdown:

```python
from functools import cache  # Python 3.9+

@cache
def solve(i, j):
    ...
```

Internally, Python creates a **dictionary keyed by the function's arguments**. When you call `solve(2, 3)`:

```
1st call  → not in cache → compute → store {(2,3): result} → return result
2nd call  → found in cache → return result instantly (O(1))
```

It only works when arguments are **hashable** — integers, strings, tuples work. Lists and dicts do not (which is why DP problems always use indices, not slices).

`@cache` vs manual `memo = {}`:

||`@cache`|Manual dict|
|---|---|---|
|Code length|1 line|4+ lines|
|Scope|Tied to function|You control it|
|Clearing|`solve.cache_clear()`|`memo.clear()`|
|In interviews|Fine to use|Shows deeper understanding|

In interviews, **implement it manually** — it shows you know what's happening. In contests, `@cache` is fine.

---

## Stage 3 preview — Tabulation (Bottom-up DP)

Memoization is **top-down** — you start at the answer and recurse down to base cases. There's another approach: **bottom-up**, where you start from base cases and build up to the answer iteratively. No recursion at all.

For Fibonacci:

```python
def fib(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[0] = 0   # base case
    dp[1] = 1   # base case
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # same recurrence, no recursion
    return dp[n]
```

Same logic, no call stack, no recursion limit issues. This is the final form of DP and what interviewers love to see.

---

**Your turn — small exercise before we go to tabulation:**

Here's the **House Robber problem** (LC #198):

> You are a robber. Houses are in a line, each with some money `nums[i]`. You can't rob two adjacent houses (alarm triggers). What's the maximum money you can rob?

Using the 3 questions, tell me:

1. What does `solve(i)` return?
2. What are the base cases?
3. What is the recurrence — if you're at house `i`, what are your two choices?

Don't code it yet — just answer those 3 questions in plain English. This is the hardest part of DP and I want to see your thinking.

Good start — you've got the right instinct on point 3. But let's sharpen all three answers because being precise here is what separates someone who _gets_ DP from someone who just memorizes patterns.

Let me push back on each one:

---

**Point 1 — "max money" is too vague.**

Max money _from where to where_? The whole array? From house `i` to the end?

The key to DP is that `solve(i)` must represent a **self-contained subproblem**. The most natural definition here is:

> `solve(i)` = maximum money you can rob **from house `i` to the last house**

This way `solve(0)` is the full answer, and `solve(i)` naturally depends on `solve(i+1)` and `solve(i+2)`.

---

**Point 2 — you skipped the base cases entirely.**

This is the most common reason DP code crashes or gives wrong answers. Ask yourself: what are the smallest inputs where you _know_ the answer without any recursion?

- `solve(n)` → no houses left → **return 0**
- `solve(n-1)` → only one house left, you must take it → **return nums[n-1]**

---

**Point 3 — "either choose i or skip it" is exactly right, but incomplete.**

You identified the two choices correctly. Now you need to say **what happens after each choice:**

- **Rob house `i`** → you gain `nums[i]`, but you _cannot_ rob house `i+1`, so you jump to `solve(i+2)`
- **Skip house `i`** → you gain nothing, move to `solve(i+1)`

You take the `max` of both because you play optimally.

---

So the full recurrence is:

```
solve(i) = max(
    nums[i] + solve(i+2),   # rob house i, skip i+1
    solve(i+1)              # skip house i
)
```

---

Now **you write the code.** Use the memoization template from above:

```python
memo = {}

def solve(i):
    # 1. base case(s)
    # 2. check cache
    # 3. compute using the recurrence
    # 4. store and return
```

Fill this in for House Robber and paste your code — don't worry about it being perfect, I want to see your attempt.