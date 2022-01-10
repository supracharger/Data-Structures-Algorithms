# python3
import sys

def BWT(text):
    M = [ ]
    # Create Matrix
    for i in range(len(text)):
        M.append(text[-i:] + text[:-i])
    # Sort Strings
    M = sorted(M)
    # Concat the last column
    return ''.join([seq[-1] for seq in M])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()

    #text = 'AA$'
    #text = 'ACACACAC$'
    #text = 'AGACATA$'

    print(BWT(text))