# Analyzing the Time Complexity of Quick Sort

The time complexity of an algorithm gives us an idea of how the runtime will increase relative to the input size.
For Quick Sort, the time complexity can be described as O(nlogn) for average and best-case scenarios. O(n^2) for the worst-case scenario.

The worst-case scenario arises when the pivot divides the array predominantly into one large sub-array and one small sub-array instead of equal halves. However, the efficient partitioning scheme ensures the average case is much more likely in practice, making Quick Sort one of the most efficient sorting algorithms in practical use.

As a workaround to achieve a higher probability of O(nlogn) complexity, the pivot can be chosen as a random element, not always as a middle one, to make the choice less deterministic.

# Analyzing the Space Complexity of Quick Sort

Space complexity refers to the amount of memory an algorithm needs to complete its run. With Quick Sort, the space complexity stems primarily from its recursive nature. Each recursive call requires additional space on the call stack, proportional to the depth of recursion. However, Quick Sort averages an excellent space complexity of O(logn).

It is possible to implement quick sort without using recursion; in that case, the additional space complexity will be
O(1).

# Analyzing the Time Complexity of Merge Sort

The time complexity of Merge Sort is O(nlogn) in all cases — best, average, and worst. This consistent efficiency is an advantage over other algorithms, such as Quick Sort, which can degrade to a time complexity of O(n^2) under unfavorable conditions.

To recap, a time complexity of O(nlogn) implies that the running time increases linear-logarithmically with the size of the input. This characteristic makes Merge Sort highly efficient at handling large data sets.

# Analyzing the Space Complexity of Merge Sort

The space complexity of Merge Sort is O(n), due to the auxiliary space used for the temporary arrays while merging the elements. This requirement is crucial to keep in mind and can be a deciding factor when selecting an algorithm in situations with limited memory.

# K-th Smallest or Largest Number

_`The k-th largest element is at position (n - k + 1) when counting from the smallest.`_

**Step-by-step derivation**

- k-th largest means there are (k-1) elements larger than it
- So there are n - (k-1) = n - k + 1 elements smaller than or equal to it
- Therefore, it's the (n - k + 1)-th smallest
