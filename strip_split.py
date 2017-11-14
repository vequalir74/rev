import sys

numLines = sys.stdin.readline()

sentence1 = [0] * int(numLines)
for i in range(0, int(numLines)):
  sentence1[i] = sys.stdin.readline().strip()

for k in range(0, int(numLines)):
  print(' '.join(j[::-1] for j in sentence1[k].split()))
