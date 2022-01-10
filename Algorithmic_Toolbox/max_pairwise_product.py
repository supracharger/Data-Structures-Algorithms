def max_pairwise_product_old(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product(numbers):
    maxA = maxB = -1
    for i,n in enumerate(numbers):
        if n > maxA:
            maxA = n
            place = i
    for i,n in enumerate(numbers):
        if n > maxB and i != place:
            maxB = n
    return maxA * maxB

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
