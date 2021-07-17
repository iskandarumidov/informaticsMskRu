# Реализуйте алгоритм бинарного поиска.

# Входные данные
# В первой строке входных данных содержатся натуральные числа N и K (0<N,K≤100000). Во второй строке задаются N элементов первого массива, отсортированного по возрастанию, а в третьей строке – K элементов второго массива. Элементы обоих массивов - целые числа, каждое из которых по модулю не превосходит 109

# Выходные данные
# Требуется для каждого из K чисел вывести в отдельную строку "YES", если это число встречается в первом массиве, и "NO" в противном случае.

# Примеры
# входные данные
# 10 5
# 1 2 3 4 5 6 7 8 9 10 
# -2 0 4 9 12 
# выходные данные
# NO
# NO
# YES
# YES
# NO



n, k = map(int, input().split())
data = list(map(int, input().split()))
targets = list(map(int, input().split()))

# n = 10
# k = 5
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# targets = [-2, 0, 4, 9, 12]


def binSearch(data, target):
  l = -1
  r = len(data)

  while l+1<r:
    m=l+(r-l)//2
    if data[m] < target:
      l = m
    else:
      r = m
  if r == len(data):
    return False
  if data[r] != target:
    return False
  return True

def solve(data, targets, n, k):
  for cur in targets:
    if binSearch(data, cur):
      print("YES")
    else:
      print("NO")

solve(data, targets, n, k)
