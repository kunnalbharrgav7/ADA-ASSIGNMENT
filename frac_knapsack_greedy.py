#  Implement the fractional knapsack problem using a greedy approach in flowchart.


1. Sort the items in descending order of their value-to-weight ratios.
2. Initialize the total value and total weight of the knapsack to zero.
3. Repeat the following steps for each item:
a. If the item can be added to the knapsack without exceeding its capacity, add it completely and update the total value and total weight of the knapsack.
b. If the item cannot be added completely, add a fraction of it that can fit and update the total value and total weight of the knapsack accordingly.
4. Return the total value of the knapsack.
