#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = {0:{ }}
    cnt = 0
    for pat in patterns:
        node = tree[0]
        j = 0
        for c in pat:
            if c in node and node[c] in tree:
                node = tree[node[c]]
            else:
                cnt += 1
                node[c] = cnt
                node = tree[cnt] = { }

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    #patterns = ['ATA']
    #patterns = ['A', 'TC']
    #patterns = ['AT', 'AG', 'AC']
    #patterns = 'ATAGA ATC GAT'.split()
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
