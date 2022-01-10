# python3


def build_heap(data):
    swaps = [ ]
    for i in range((len(data)-1)//2, -1, -1):
        SiftDown(i, data, swaps)
    return swaps

def SiftDown(i, H, swaps):
    maxIdx = i
    # Left Child
    left = 2 * i + 1       
    if left < len(H) and H[left] < H[maxIdx]:
        maxIdx = left
    # Right Child
    right = 2 * i + 2
    if right < len(H) and H[right] < H[maxIdx]:
        maxIdx = right
    # Swap
    if i != maxIdx:
        H[i], H[maxIdx] = H[maxIdx], H[i]
        swaps.append((i, maxIdx))
        SiftDown(maxIdx, H, swaps)
    

def build_heap_old(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    # data = [5,4,3,2,1]
    # data = [1,2,3,4,5]

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
