def binary_search(keys, query):
    def binary_search_inner(l, r):
        if l > r:
            return -1

        index = (l + r)//2

        key = keys[index]
        if key == query:
            return index
        elif key > query:
            return binary_search_inner(l, index-1)
        else:
            return binary_search_inner(index+1, r)

    return binary_search_inner(0, len(keys)-1)


def binary_search_naive(keys, query):
    keys_len = len(keys)
    q = query
    key_index = -1
    for j in range(keys_len):
        if keys[j] == q:
            key_index = j
            break
    return key_index


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
