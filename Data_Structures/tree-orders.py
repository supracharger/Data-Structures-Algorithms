# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    #inp = ['4 1 2', '2 3 4', '5 -1 -1', '1 -1 -1', '3 -1 -1']
    #inp = '0 7 2;10 -1 -1;20 -1 6;30 8 9;40 3 -1;50 -1 -1;60 1 -1;70 5 4;80 -1 -1;90 -1 -1'.split(';')
    #self.n = len(inp)

    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]

    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      # [a, b, c] = map(int, inp[i].split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    def inOrderSub(ix):
      if self.left[ix] >= 0:
        inOrderSub(self.left[ix])
      self.result.append(self.key[ix])
      if self.right[ix] >= 0:
        inOrderSub(self.right[ix])
    inOrderSub(0)         
    return self.result

  def preOrder(self):
    self.result = []
    def preOrderSub(ix):
      self.result.append(self.key[ix])
      if self.left[ix] >= 0:
        preOrderSub(self.left[ix])
      if self.right[ix] >= 0:
        preOrderSub(self.right[ix])
    preOrderSub(0)          
    return self.result

  def postOrder(self):
    self.result = []
    def postOrderSub(ix):
      if self.left[ix] >= 0:
        postOrderSub(self.left[ix])
      if self.right[ix] >= 0:
        postOrderSub(self.right[ix])
      self.result.append(self.key[ix])
    postOrderSub(0)                
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
