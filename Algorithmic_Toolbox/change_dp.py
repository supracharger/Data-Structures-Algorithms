# Uses python3
import sys

# Cited: https://www.youtube.com/watch?v=jgiZlGzXMBw
def get_change(m):
    mini = [0] * (m+1)
    change = [1, 3, 4]
    for i in range(1, m+1):
        mn = float('inf')
        for c in change:
            if i-c >= 0:
                mn = min(mn, mini[i-c] + 1)
        mini[i] = mn
    return mini[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = 34
    print(get_change(m))
