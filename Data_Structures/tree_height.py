# python3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    parents = np.array(parents, dtype=int)
    found = [None] * len(parents)
    return FindReferIdx(np.where(parents == -1)[0][0], parents, found)

def FindReferIdx(find, parents, found):
    if found[find] != None:
        return found[find]
    idx = np.where(parents == find)[0]
    heights = [FindReferIdx(i, parents, found) for i in idx]
    heights.append(0)       # Floor of zero
    value = max(heights) + 1
    found[find] = value
    return value

def compute_height_old2(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def main():
    #n = int(input())
    #parents = list(map(int, input().split()))
    
    parents = [4,-1,4,1,1]
    #parents = [-1,0,4,0,3]
    #parents = [9,7,5,5,2,9,9,9,2,-1]    # output: 4
    n = len(parents)

    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
