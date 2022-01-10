# Uses python3
def edit_distance(s, t):
    dist = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    # Constant Numbers
    for i in range(1, len(s)+1):
        dist[i][0] = i
    for j in range(1, len(t)+1):
        dist[0][j] = j
    # Calc rest of matrix
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            mismatch = 0 if s[i-1] == t[j-1] else 1
            dist[i][j] = min(   dist[i][j-1] + 1,           # Insertion
                                dist[i-1][j] + 1,           # deletion
                                dist[i-1][j-1] + mismatch)  # match/ mismatch
    #write your code here
    return dist[len(s)][len(t)]

if __name__ == "__main__":
    #print(edit_distance('ab', 'ab'))
    #print(edit_distance('short', 'ports'))
    #print(edit_distance('editing', 'distance'))
    print(edit_distance(input(), input()))
