# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    pass

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

# help with solution: https://stackoverflow.com/questions/36972714/implementing-3-way-quicksort
def randomized_quick_sort(a, l, r):
    for i,v in enumerate(quick_sorts(a)):
        a[i] = v

def quick_sorts(a):
    if len(a) <= 1: return a
    k = random.randint(0, len(a)-1)
    x = a[k]
    under, equal, over = [], [], []
    for v in a:
        if v < x: under.append(v)
        elif v == x: equal.append(v)
        elif v > x: over.append(v)
    return quick_sorts(under) + equal + quick_sorts(over)

def randomized_quick_sort_old(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #a = [2,3,9,2,2]
    #n = len(a)
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
