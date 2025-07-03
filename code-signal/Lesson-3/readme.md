# Analyzing the Time Complexity of Quick Sort

The time complexity of an algorithm gives us an idea of how the runtime will increase relative to the input size.
For Quick Sort, the time complexity can be described as O(nlogn) for average and best-case scenarios. O(n^2) for the worst-case scenario.

The worst-case scenario arises when the pivot divides the array predominantly into one large sub-array and one small sub-array instead of equal halves. However, the efficient partitioning scheme ensures the average case is much more likely in practice, making Quick Sort one of the most efficient sorting algorithms in practical use.

As a workaround to achieve a higher probability of O(nlogn) complexity, the pivot can be chosen as a random element, not always as a middle one, to make the choice less deterministic.

# Analyzing the Space Complexity of Quick Sort

Space complexity refers to the amount of memory an algorithm needs to complete its run. With Quick Sort, the space complexity stems primarily from its recursive nature. Each recursive call requires additional space on the call stack, proportional to the depth of recursion. However, Quick Sort averages an excellent space complexity of O(logn).

It is possible to implement quick sort without using recursion; in that case, the additional space complexity will be
O(1).
