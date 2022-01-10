# Uses python3
import sys

def optimal_weight(W, w):
    score = [([0] * (len(w)+1)) for _ in range(W+1)]
    for j in range(1, len(w)+1):
        for i in range(1, W+1):
            result = i - w[j-1]
            if result >= 0:
                score[i][j] = max(score[result][j-1] + w[j-1],
                                    score[i][j-1])
            else:
                score[i][j] = score[i][j-1]
    return score[W][len(w)]

def optimal_weight_old(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    #W, w = 10, [1, 4, 8]
    print(optimal_weight(W, w))
