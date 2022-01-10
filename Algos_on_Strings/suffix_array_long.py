# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  order = SortCharacters(text)
  clss = ComputeCharClasses(text, order)
  L = 1
  while L < len(text):
    order = SortDoubled(text, L, order, clss)
    clss = UpdateClasses(order, clss, L)
    L *= 2
  # Implement this function yourself
  return order

def SortCharacters(S):
  order = [0] * len(S)
  count = [0] * 5
  toIndex = {c:i for i,c in enumerate('$ACGT')}
  sIdx = [ ]
  for st in S:
    ii = toIndex[st]
    # ii = ord(st) - 64
    # if ii < 0: ii = 0
    count[ii] += 1
    sIdx.append(ii)
  for i in range(1, len(count)):
    count[i] += count[i-1]
  for i in range(len(S)-1, -1, -1):
    c = sIdx[i]
    count[c] -= 1
    order[count[c]] = i
  return order

def ComputeCharClasses(S, order):
  clss = [0] * len(S)
  for i in range(1, len(S)):
    if S[order[i]] != S[order[i-1]]:
      clss[order[i]] = clss[order[i-1]] + 1
    else:
      clss[order[i]] = clss[order[i-1]]
  return clss

def SortDoubled(S, L, order, clss):
  count = [0] * len(S)
  newOrder = [0] * len(S)
  for i in range(len(S)):
    count[clss[i]] += 1
  for i in range(1, len(S)):
    count[i] += count[i-1]
  for i in range(len(S)-1, -1, -1):
    start = (order[i] - L + len(S)) % len(S)
    cl = clss[start]
    count[cl] -= 1
    newOrder[count[cl]] = start
  return newOrder

def UpdateClasses(newOrder, clss, L):
  n = len(newOrder)
  newClass = [0] * n
  for i in range(1, n):
    cur, prev = newOrder[i], newOrder[i-1]
    mid, midPrev = (cur+L), (prev+L) % n
    if clss[cur]!=clss[prev] or clss[mid]!=clss[midPrev]:
      newClass[cur] = newClass[prev] + 1
    else:
      newClass[cur] = newClass[prev]
  return newClass

if __name__ == '__main__':
  text = sys.stdin.readline().strip()

  #text = 'AAA$'
  ##text = 'GAC$'
  #text = 'GAGAGAGA$'
  #text = 'AACGATAGCGGTAGA$'
  
  print(" ".join(map(str, build_suffix_array(text))))
