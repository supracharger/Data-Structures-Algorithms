def binary_search(keys, query):
    return binary(keys, 0, len(keys)-1, query)

def binary(keys, low, high, find):
    if high < low: return -1
    pivot = low + int((high - low)/2)
    x = keys[pivot]
    if x == find: return pivot
    elif find < x:
        return binary(keys, low, pivot-1, find)
    elif find > x:
        return binary(keys, pivot+1, high, find)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries
    #input_keys, input_queries = [1,5,8,12,13], [8,1,23,1,11]
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
