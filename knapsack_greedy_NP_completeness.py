# Implement a greedy algorithm for the Knapsack Problem.

def knapsack_greedy(values, weights, capacity):
    # calculate value-to-weight ratios
    ratios = [v/w for v, w in zip(values, weights)]
    # sort items by ratio in decreasing order
    items = sorted(zip(ratios, values, weights), reverse=True)
    # initialize total value and weight of items in knapsack
    total_value = 0
    total_weight = 0
    # iterate over sorted items and add to knapsack if possible
    for ratio, value, weight in items:
        if total_weight + weight <= capacity:
            total_value += value
            total_weight += weight
        else:
            # knapsack is full
            break
    return total_value
