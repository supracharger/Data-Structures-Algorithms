# Uses python3
import sys

# Help for found solution: https://www.cuemath.com/numbers/lcm-least-common-multiple/
def lcm_naive(a, b):
    return int(a * b / gcd(a, b))

def lcm_naive_old(a, b):
    for l in range(1, min(a,b) + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    if a == 0: return b
    elif b == 0: return a
    a2 = min(a, b)
    b2 = max(a, b) % a2
    return gcd(a2, b2)

if __name__ == '__main__':
    # import numpy as np
    # for ii in range(1000):
    #     a = np.random.randint(3, 100)
    #     b = np.random.randint(3, 100)
    #     w1 = lcm_naive(a, b)
    #     w2 = lcm_naive_old(a, b)
    #     if w1 != w2:
    #         print(w1, '!=', w2, ':', (a, b))
    #         break
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

