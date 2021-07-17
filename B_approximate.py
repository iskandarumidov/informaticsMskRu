# n = 5
# k = 5
# data = [1, 3, 5, 7, 9, 15]
# targets = [2, 4, 8, 1, 6]
# targets = [10, 14]

n, k = map(int, input().split())
data = list(map(int, input().split()))
targets = list(map(int, input().split()))

def binSearch(data, target):
  l = -1
  r = len(data)

  while l+1<r:
    m=l+(r-l)//2
    if data[m] < target:
      l = m
    else:
      r = m
  # print(l, m, r)
  if r == len(data):
    return data[l]
  if l == -1:
    return data[r]
  if abs(data[r]-target) < abs(data[l]- target):
    return data[r]
  return data[l]
  # return min(abs(data[r]-target), abs(data[l]- target))
  
def solve(data, targets):
  for cur in targets:
    print(binSearch(data, cur))

solve(data, targets)