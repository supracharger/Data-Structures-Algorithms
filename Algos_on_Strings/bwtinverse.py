# python3
import sys

def InverseBWT(bwt):
    # Get first and last columns    
    last = list(bwt)
    first = sorted(list(last))
    # Labels symbols with a ctr to when the number appeared
    first, last = LabedSymbols(first), LabedSymbols(last)
    # Denote first to last
    D = {f:last[i] for i,f in enumerate(first)}
    key = D[('$', 1)]
    text = [key[0]]
    # find origonal text
    while key != ('$', 1):
        key = D[key]
        text.append(key[0])
    return ''.join(text[:-1][::-1]) + '$'

def LabedSymbols(values):
    symbols = [ ]
    cnt = { }
    for v in values:
        if not v in cnt.keys():
            cnt[v] = 1
        c = cnt[v]
        cnt[v] = c + 1
        symbols.append((v, c))
    return symbols

if __name__ == '__main__':
    #bwt = sys.stdin.readline().strip()
    bwt = 'annb$aa'
    #bwt = 'AC$A'
    #bwt = 'AGGGAA$'
    print(InverseBWT(bwt))