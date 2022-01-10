# python3
import sys

class Node:
	def __init__ (self, idx):
		self._idx = idx
		self.patternEnd = False
	
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
		if nd.patternEnd: 			# is leaf node
			return True
		else:						# is Edge
			v = branch
	return False

def ConstructTrie(patterns):
	root = [{}]
	for pat in patterns:
		node = root[0]
		prevNode = None
		for c in pat:
			if c in node:
				ix = node[c]._idx
				prevNode = node[c]
				node = root[ix]
			else:
				node[c] = prevNode = Node(len(root))
				node = { }
				root.append(node)
		prevNode.patternEnd = True
	return root

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

#text, patterns = 'AAA', 'AA'.split()
#text, patterns = 'ACATA', 'AT A AG'.split()
#n = len(patterns)

ans = solve (text, n, patterns)
sys.stdout.write (' '.join (map (str, ans)) + '\n')
