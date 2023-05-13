#  Implement the knapsack problem using a greedy approach in Python.


def knapsack_greedy(capacity, items):
    """
    Solve the knapsack problem using a greedy approach.

    :param capacity: the capacity of the knapsack
    :param items: a list of tuples representing the items, where each tuple contains (value, weight)
    :return: the maximum value that can be obtained
    """
    # sort items by value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    max_value = 0
    current_weight = 0

    for value, weight in sorted_items:
        if current_weight + weight <= capacity:
            max_value += value
            current_weight += weight
        else:
            remaining_capacity = capacity - current_weight
            max_value += value * (remaining_capacity / weight)
            break

    return max_value
