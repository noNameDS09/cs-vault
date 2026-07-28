| Sorting Algorithm  | Best Case                      | Average Case   | Worst Case     | Stable                           | In-place                                |
| ------------------ | ------------------------------ | -------------- | -------------- | -------------------------------- | --------------------------------------- |
| **Bubble Sort**    | **O(n)** _(optimized version)_ | **O(n²)**      | **O(n²)**      | Yes                              | Yes                                     |
| **Selection Sort** | **O(n²)**                      | **O(n²)**      | **O(n²)**      | No                               | Yes                                     |
| **Insertion Sort** | **O(n)**                       | **O(n²)**      | **O(n²)**      | Yes                              | Yes                                     |
| **Merge Sort**     | **O(n log n)**                 | **O(n log n)** | **O(n log n)** | Yes                              | No (requires O(n) extra space)          |
| **Quick Sort**     | **O(n log n)**                 | **O(n log n)** | **O(n²)**      | No                               | Yes (recursive stack: O(log n) average) |
| **Radix Sort**     | **O(nk)**                      | **O(nk)**      | **O(nk)**      | Yes (if stable sub-sort is used) | No (typically requires extra space)     |