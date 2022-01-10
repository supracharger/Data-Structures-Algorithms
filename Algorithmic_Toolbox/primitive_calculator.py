# Uses python3
import sys

def optimal_sequence(n):
    op = [0] * (n+1)
    mini = [0] * (n+1)
    actions = [1, 2, 3]
    op[1] = 1
    for i in range(2, n+1):
        mn = float('inf')
        for act in actions:
            if act == 1:
                result = i - 1
            else:
                result = i // act
                if i / act != i // act: continue
            cnt = mini[result] + 1
            if cnt < mn:
                mn = mini[i] = cnt
                op[i] = act
    return create_sequence(op, n)

def create_sequence(op, n):
    series = [n]
    while n > 1:
        act = op[n]
        if act == 1:
            n -= 1
        else:
            n //= act
        series.insert(0, n)
    return series

def optimal_sequence_old(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
#n = 1
#n = 5
#n = 96234
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
