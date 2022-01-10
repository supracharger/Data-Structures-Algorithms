#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  if len(tree) > 0:
    return SubBinarySearchTree(0, tree, -2147483650, 2147483650)
  return True

def SubBinarySearchTree(loc, tree, mn, mx):
  node = tree[loc]
  value = node[0]
  if value < mn or value > mx:
    return False
  # Left Side
  left = right = True
  if node[1] >= 0:
    left = SubBinarySearchTree(node[1], tree, mn, value - 1)
  # Right Side
  if node[2] >= 0:
    right = SubBinarySearchTree(node[2], tree, value + 1, mx)
  return left and right


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))

  #tree = '2 1 2;1 -1 -1;3 -1 -1'
  #tree = '1 1 2;2 -1 -1;3 -1 -1'
  #tree = '1 -1 1;2 -1 2;3 -1 3;4 -1 4;5 -1 -1'
  #tree = '4 1 2;2 3 4;6 5 6;1 -1 -1;3 -1 -1;5 -1 -1;7 -1 -1'
  #tree = '4 1 -1;2 2 3;1 -1 -1;5 -1 -1'
  #tree = [[int(num) for num in node.split()] for node in tree.split(';')]
  #nodes = len(tree)

  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
