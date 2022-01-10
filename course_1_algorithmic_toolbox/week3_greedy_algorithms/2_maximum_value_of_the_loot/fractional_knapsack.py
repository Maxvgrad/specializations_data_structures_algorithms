# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    def get_optimal_value_inner(capacity, items, value_accumulated):
        if capacity == 0 or len(items) == 0:
            return round(value_accumulated, 3)
        item = items.pop()
        weight_to_grab = item.total_weight

        if weight_to_grab > capacity:
            weight_to_grab = capacity

        return get_optimal_value_inner(capacity - weight_to_grab, items, value_accumulated + weight_to_grab * item.get_value_per_weight())

    items = []
    for i in range(len(weights)):
        item = Item()
        item.total_value = values[i]
        item.total_weight = weights[i]
        items.append(item)

    items.sort(key=get_sort_key)

    return get_optimal_value_inner(capacity, items, 0)


class Item:
    total_weight = -1
    total_value = 0

    def get_value_per_weight(self):
        return self.total_value / self.total_weight


def get_sort_key(item):
    return item.get_value_per_weight()

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
