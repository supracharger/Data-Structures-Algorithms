# Uses python3
import sys

# Help to understand solution: https://www.cuemath.com/numbers/greatest-common-divisor-gcd/
def gcd_naive(a, b):
    if a == 0: return b
    elif b == 0: return a
    a2 = min(a, b)
    b2 = max(a, b) % a2
    return gcd_naive(a2, b2)

def gcd_naive_old(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

if __name__ == "__main__":
    # import numpy as np
    # # input = sys.stdin.read()
    # while True:
    #     a = np.random.randint(3, 100)
    #     b = np.random.randint(3, 100)
    #     w1 = gcd_naive(a, b)
    #     w2 = gcd_naive_old(a, b)
    #     if w1 != w2:
    #         print(w1, '!=', w2, ':', (a, b))
    #         break
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
