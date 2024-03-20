arr = [1, 2, 3, 4]
arr2 = map(lambda x: x ** 2, arr)
print(list(arr))

arr3 = filter(lambda x: x % 2 == 0, arr)
print(list(arr3))

sum = sum(arr)
print(sum)