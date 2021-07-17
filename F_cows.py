n, cows = map(int, input().split())

stables = list(map(int, input().split()))

def isValid(stables, cows, m):
  cows-=1
  prevCow = stables[0]
  for i in range(1, len(stables)):
    prevDist = stables[i]-prevCow
    if prevDist >= m:
      cows-=1
      prevCow = stables[i]
  return cows <= 0

def getMinDistance(stables, cows):
  l = 0
  r = stables[-1]-stables[0]+1

  while l+1<r:
    m=l+(r-l)//2

    if isValid(stables, cows, m):
      l = m
    else:
      r = m
  return l

print(getMinDistance(stables, cows))