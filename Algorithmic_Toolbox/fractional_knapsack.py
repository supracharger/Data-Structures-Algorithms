# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    frac = [values[i] / wt for i,wt in enumerate(weights)]
    # Sort by index by 'frac' DESC
    sortIx = list(sorted(range(len(weights)), key=lambda i: frac[i]))
    for i in sortIx[::-1]:
        add = min(weights[i], capacity)
        capacity -= add
        value += frac[i] * add
        if capacity == 0: break
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    """ #
    capacity = 50
    values = [60, 100, 120]
    weights = [20, 50, 30] 
    #
    capacity = 10
    values = [500]
    weights = [30]"""
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
