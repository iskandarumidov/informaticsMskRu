# n = 3
# k = 4
# data = [1, 1, 2, 2, 2, 4]
# targets = [2, 4, 8, 1, 6]
# targets = [2]

n = input()
data = list(map(int, input().split()))
m = input()
targets = list(map(int, input().split()))

def lowerBinSearch(data, target):
  l = -1
  r = len(data)

  while l+1<r:
    m=l+(r-l)//2
    if data[m] < target:
      l = m
    else:
      r = m
  # print(l, m, r)
  # if r == len(data):
  #   return 0
  # if data[r] != target:
  #   return False
  # return True
  return r

def upperBinSearch(data, target):
  l = -1
  r = len(data)

  while l+1<r:
    m=l+(r-l)//2
    if data[m] <= target:
      l = m
    else:
      r = m
  # print(l, m, r)  
  return r
  # if r == len(data):
  #   return False
  # if data[r] != target:
  #   return False
  # return True
  
def solve(data, targets):
  data.sort()
  for cur in targets:
    low = lowerBinSearch(data, cur)
    up = upperBinSearch(data, cur)
    print(up-low, end =" ")

solve(data, targets)