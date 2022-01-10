# python3
import sys

def ComputePrefixFunction(P):
  s = [0] * len(P)
  boarder = 0
  for i in range(1, len(P)):
    while boarder > 0 and P[i] != P[boarder]:
      boarder = s[boarder - 1]
    if P[i] == P[boarder]:
      boarder += 1
    else:
      boarder = 0
    s[i] = boarder
  return s

def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  S = pattern + '$' + text
  s = ComputePrefixFunction(S)
  result = []
  for i in range(len(pattern), len(S)):
    if s[i] == len(pattern):
      result.append(i - 2 * len(pattern))
  # Implement this function yourself
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()

  #pattern, text = 'TACG', 'GT'
  #pattern, text = 'ATA', 'ATATA'
  #pattern, text = 'ATAT', 'GATATATGCATATACTT'

  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

