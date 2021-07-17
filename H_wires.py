n, k = map(int, input().split())

wires = []
for i in range(n):
  wires.append(int(input()))


def isValid(n, k, wires, target):
  total = 0
  for cur in wires:
    total += (cur // target)
  
  return total >= k

  
def solve(n, k, wires):
  l = 0
  r = 10**7+1

  while l+1<r:
    m=l+(r-l)//2

    if isValid(n, k, wires, m):
      l = m
    else:
      r = m
  return l

print(solve(n, k, wires))