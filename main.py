import math

preprev = 1
prev = 1
for i in range(1, 60):
  res = -5 / i
  print("a"+str(i), res, sep=": ")
  preprev = prev
  prev = res

# print(13/38)

# def getHaveCeil(num):
#   for i in range(-20, 20):
#     res = False
#     for j in range(1, 100):
#       if (((40 * j + i)/(41 * j - 1))>num):
#         res = True
#     print(i, res, sep=": ")

# getHaveCeil(1)