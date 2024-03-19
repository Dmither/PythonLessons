def counter():
  count = 0
  def increase():
    nonlocal count
    count += 1
    return count
  return increase

counter1 = counter()
print(counter1())
print(counter1())
print(counter1())

counter2 = counter()
print(counter2())
print(counter2())
print(counter2())