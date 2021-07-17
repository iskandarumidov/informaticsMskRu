n, x, y = map(int, input().split())

def isValidTime(time, n, x, y):
  curTime = 0
  curTime += min(x, y)
  n-=1
  firstCopies = (time-curTime) // x
  secondCopies = (time-curTime) // y
  return firstCopies+secondCopies >= n

def binSearch(n, x, y):
  l = 0
  r = 2*(10**9)

  while l+1<r:
    m=l+(r-l)//2
    if isValidTime(m, n, x, y):
      r = m
    else:
      l = m
  return r

def solve(n, x, y):
  print(binSearch(n, x, y))

solve(n, x, y)
