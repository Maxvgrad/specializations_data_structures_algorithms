# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    cache = {}

    for i in range(0, len(parents)):
        key = str(parents[i])
        if key not in cache:
            cache[key] = []
        cache[key].append(str(i))

    def get_height(node_label):
        if node_label not in cache:
            cache[node_label] = []
        children = cache[node_label]
        max_depth = 0
        if len(children) == 0:
            return 0

        for child_label in children:
            depth = get_height(child_label)
            if max_depth < depth:
                max_depth = depth

        return 1 + max_depth
    return get_height('-1')


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
