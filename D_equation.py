# ax3+bx2+cx+d=0

# a = 1
# b = -3
# c = 3
# d = -1

a, b, c, d = map(int, input().split())

def functionAtX(a, b, c, d, x):
  curSol = a*(x**3)+b*(x**2)+c*(x)+d
  return curSol

def binSearch(a, b, c, d):
  l = -1
  r = 1

  while functionAtX(a, b, c, d, l) >= 0 or functionAtX(a, b, c, d, r) <= 0:
    l = l*2
    r = r*2
  # print(l, m, r)
  

  for i in range(60):
    m = l+(r-l)/2
    if functionAtX(a, b, c, d, m) < 0:
      l = m
    else:
      r = m
  return r
    
  # print(l, m, r)
  
def solve(a, b, c, d):
  if a < 0:
    b*=-1
    c*=-1
    d*=-1
    a*=-1
  print(binSearch(a, b, c, d))

solve(a, b, c, d)