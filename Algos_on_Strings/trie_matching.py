# python3
import sys

NA = -1

class Node:
	def __init__ (self, idx):
		self._idx = idx
		# self.next = [NA] * 4
	
	def __repr__(self):
		return 'Node_' + str(self._idx)

def solve (text, n, patterns):
	result = []
	trie = ConstructTrie(patterns)
	for k in range(len(text)):
		foundIx = PrefixTireMatching(text[k:], trie)
		if not foundIx: continue				# Did not find substring
		result.append(k)
	return result

def PrefixTireMatching(text, trie):
	v = trie[0]
	for i,sym in enumerate(text):
		try: 
			nd = v[sym]
			branch = trie[nd._idx]
		except KeyError: return False
		if len(branch) == 0: 		# is leaf node
			return True
		else:						# is Edge
			v = branch
	return False



def ConstructTrie(patterns):
	root = [{}]
	for pat in patterns:
		node = root[0]
		for c in pat:
			if c in node:
				ix = node[c]._idx
				node = root[ix]
			else:
				node[c] = Node(len(root))
				node = { }
				root.append(node)
	return root

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

#patterns = ['AT', 'AG', 'AC']
#trie = ConstructTrie(patterns)
#text, patterns = 'AAA', 'AA'.split()
#text, patterns = 'AA', 'T'.split()
#text, patterns = 'AATCGGGTTCAATCGGGGT', 'ATCG GGGT'.split()
#n = len(patterns)

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
