c = float(input())

def findX(c):
  l = 0
  r = c

  for i in range(60):
    m = l+(r-l)/2

    if m*m + m**(0.5) > c:
      r = m
    else:
      l = m
  return r

print(findX(c))
