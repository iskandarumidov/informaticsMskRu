m, n = map(int, input().split())

workers = []
for i in range(n):
  workers.append(list(map(int, input().split())))
workerBalls = [0]*len(workers)

def isValid(n, k, workers, target, workerBalls):
  totalBalls = 0
  for i in range(len(workers)):
    cur = workers[i]
    curBalls = 0
    cycle = cur[0]*cur[1] + cur[2]
    curBalls+=(target//cycle)*cur[1]
    remain = target % cycle
    curBalls+=remain // cur[0]
    totalBalls+=curBalls
    workerBalls[i] = curBalls
  # print(totalBalls, k)
  return totalBalls >= k
  
def solve(n, k, workers):
  l = 0
  r = 15000*200
  
  while l+1<r:
    m=l+(r-l)//2

    if isValid(n, k, workers, m, workerBalls):
      r = m
    else:
      l = m
  return r

print(solve(n, m, workers))
for cur in workerBalls:
  print(cur, end=" ")