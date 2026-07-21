If you're solving DSA problems in Python (especially on LeetCode, Codeforces, AtCoder, or interviews), the biggest "shortcuts" come from knowing the standard library and common coding patterns. Here are the most useful ones.

### 1. Fast input

```python
import sys
input = sys.stdin.readline
```

Read multiple integers:

```python
n, m = map(int, input().split())
arr = list(map(int, input().split()))
```

### 2. Useful imports

```python
from collections import *
from heapq import *
from bisect import *
from itertools import *
from math import *
```

Common ones:

```python
from collections import deque, Counter, defaultdict
from heapq import heappush, heappop
```

### 3. List initialization

2D list:

```python
grid = [[0] * m for _ in range(n)]
```

Avoid:

```python
grid = [[0] * m] * n   # Wrong
```

### 4. Reverse a list

```python
arr.reverse()      # In-place
arr[::-1]          # New list
```

### 5. Sorting

Ascending:

```python
arr.sort()
```

Descending:

```python
arr.sort(reverse=True)
```

Sort by second element:

```python
arr.sort(key=lambda x: x[1])
```

### 6. Frequency counting

```python
from collections import Counter

cnt = Counter(arr)

print(cnt[5])
```

Without Counter:

```python
from collections import defaultdict

freq = defaultdict(int)

for x in arr:
    freq[x] += 1
```

### 7. Queue (BFS)

```python
from collections import deque

q = deque([start])

while q:
    node = q.popleft()
```

### 8. Stack

```python
stack = []

stack.append(x)
x = stack.pop()
```

### 9. Min Heap

```python
from heapq import *

heap = []

heappush(heap, 5)
heappush(heap, 2)

x = heappop(heap)
```

Max heap:

```python
heappush(heap, -x)
x = -heappop(heap)
```

### 10. Binary Search

```python
from bisect import bisect_left, bisect_right

idx = bisect_left(arr, x)
idx = bisect_right(arr, x)
```

### 11. Prefix Sum

```python
prefix = [0]

for x in arr:
    prefix.append(prefix[-1] + x)

# sum(l, r)
ans = prefix[r + 1] - prefix[l]
```

### 12. Enumerate

Instead of:

```python
for i in range(len(arr)):
```

Use:

```python
for i, x in enumerate(arr):
```

### 13. Simultaneous iteration

```python
for a, b in zip(arr1, arr2):
    print(a, b)
```

### 14. Swap

```python
a, b = b, a
```

### 15. Maximum and Minimum

```python
mx = max(arr)
mn = min(arr)
```

### 16. Infinity

```python
INF = float('inf')
NEG_INF = float('-inf')
```

### 17. Check membership

Instead of:

```python
if x in list:
```

Use:

```python
s = set(arr)

if x in s:
```

Average lookup:

- List → O(n)
    
- Set → O(1)
    

### 18. Dictionary default

```python
from collections import defaultdict

graph = defaultdict(list)

graph[u].append(v)
```

### 19. Graph creation

```python
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
```

### 20. Matrix directions

```python
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

for dx, dy in dirs:
    nx = x + dx
    ny = y + dy
```

### 21. Memoization

```python
from functools import lru_cache

@lru_cache(None)
def dfs(i):
    ...
```

Or (Python 3.9+):

```python
from functools import cache

@cache
def dfs(i):
    ...
```

### 22. One-line condition

```python
ans = a if a > b else b
```

### 23. List Comprehension

```python
squares = [x*x for x in range(10)]

even = [x for x in arr if x % 2 == 0]
```

### 24. String to List

```python
chars = list(s)
```

Join back:

```python
s = ''.join(chars)
```

### 25. Greatest Common Divisor

```python
from math import gcd

g = gcd(a, b)
```

LCM:

```python
from math import lcm
```

### 26. Common interview template

```python
from collections import deque, Counter, defaultdict
from heapq import *
from bisect import *
from functools import cache
from math import *

class Solution:
    def solve(self, nums):
        pass
```

### 27. Time complexities worth memorizing

|Operation|Complexity|
|---|---|
|List append|O(1)|
|List pop()|O(1)|
|List pop(0)|O(n)|
|deque append/popleft|O(1)|
|Set lookup|O(1) average|
|Dict lookup|O(1) average|
|Heap push/pop|O(log n)|
|Sort|O(n log n)|
|Binary search|O(log n)|

### 28. Most-used DSA patterns

- Two pointers
    
- Sliding window
    
- Prefix sum
    
- Binary search
    
- DFS/BFS
    
- Monotonic stack
    
- Heap (priority queue)
    
- Union-Find (DSU)
    
- Dynamic Programming
    
- Backtracking
    

If you master these patterns and the associated Python shortcuts, you'll be able to solve the majority of medium-level DSA problems efficiently.