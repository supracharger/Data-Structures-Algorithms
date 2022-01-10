import re

def mini_max(i, j, operations, setMin, setMax):
    mn = float('inf')
    mx = float('-inf')
    for k in range(i, j):
        a = evalt(setMax[i][k], setMax[k+1][j], operations[k])
        b = evalt(setMax[i][k], setMin[k+1][j], operations[k])
        c = evalt(setMin[i][k], setMax[k+1][j], operations[k])
        d = evalt(setMin[i][k], setMin[k+1][j], operations[k])
        mn = min(mn, a, b, c, d)
        mx = max(mx, a, b, c, d)
    return mn, mx

def get_maximum_value(dataset):
    digits, operations = Split(dataset)
    # Fill Subsets
    setMin, setMax = init_sets(digits)
    # s[0][0], s[1][1]
    for s in range(1, len(digits)):
        for i in range(len(digits)-s):
            j = i + s
            setMin[i][j], setMax[i][j] = mini_max(i, j, operations, setMin, setMax)
    # for i in range(len(digits)-1):
    #     subset[i][i+1] = evalt(subset[i][i], subset[i+1][i+1], operations[i])
    #write your code here
    return setMax[0][len(digits)-1]

def init_sets(digits):
    setMin, setMax = [ ], [ ]
    for i,v in enumerate(digits):
        ar = [0] * len(digits)
        ar[i] = v
        setMin.append(ar)
        setMax.append(list(ar))
    return setMin, setMax

def Split(data):
    digits = [int(d) for d in re.findall(r'\d+', data)]
    operations = re.findall(r'\D+', data)
    return digits, operations

# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

if __name__ == "__main__":
    dataset = input()
    #dataset = '1+5'
    #dataset = '5-8+7*4-8+9'
    print(get_maximum_value(dataset))
