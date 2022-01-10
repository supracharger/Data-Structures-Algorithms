# Uses python3
import sys

values = [0, 1]

# Help to find solution: https://www.geeksforgeeks.org/program-find-last-digit-nth-fibonnaci-number/
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    prev, current = 0, 1
    for i in range(len(values), 60):
        prev, current = current, current + prev
        values.append(current % 10)
    return values[n % 60]

def get_fibonacci_last_digit_naive_old(n):
    if n <= 1:
        return n
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    # for num in [5, 12, 12, 24, 24, 30, 51, 52]:
    #     print(get_fibonacci_last_digit_naive(num), get_fibonacci_last_digit_naive_old(num))
    # input = sys.stdin.read()
    # print(get_fibonacci_last_digit_naive(3))
    for num in range(239):
        a = get_fibonacci_last_digit_naive(num)
        b = get_fibonacci_last_digit_naive_old(num)
        if a != b: 
            print(a, '!=', b, 'n=%d' % num)
            break
    # print(get_fibonacci_last_digit_naive(239))
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
