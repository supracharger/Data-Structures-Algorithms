def binary_search(keys, query):
    return binary(keys, 0, len(keys)-1, query)

def binary(keys, low, high, find):
    if high < low: return -1
    pivot = low + int((high - low)/2)
    x = keys[pivot]
    if x == find: 
        if pivot > 0 and keys[pivot-1] == find:
            return FindOccurs(keys, 0, pivot-1, find, pivot)
        else: return pivot
    elif find < x:
        return binary(keys, low, pivot-1, find)
    elif find > x:
        return binary(keys, pivot+1, high, find)

def FindFirstOccur(keys, idx, find):
    ii = idx
    for j in range(idx-1, -1, -1):
        if keys[j] == find:
            ii = j
        else: break
    return ii

def FindOccurs(keys, low, high, find, idx):
    if high < low: return idx
    pivot = low + int((high - low)/2)
    x = keys[pivot]
    if x == find:
        return FindOccurs(keys, low, pivot-1, find, pivot)
    else: 
        return FindOccurs(keys, pivot+1, high, find, idx)

if __name__ == '__main__':
    """"""
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries
    #input_keys, input_queries = [2,4,4,4,7,7,9], [9,4,5,2]
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
