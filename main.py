# my_list = list((1, 2, 3))
# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

class PowTwo:
  def __init__(self, max=0):
    self.max = max
  def __iter__(self):
    self.n = 0
    return self
  def __next__(self):
    if self.n <= self.max:
      result = 2 ** self.n
      self.n += 1
      return result
    else:
      raise StopIteration
    
numbers = PowTwo(3)

for num in numbers:
  print(num)

# class MyList(list):
#   def __next__(self):
#     print("Hello")
#     super().__next__(self)

# my_list_2 = MyList((1, 2, 3))
# iterator2 = iter(my_list_2)
# print(next(iterator2))
# print(next(iterator2))
# print(next(iterator2))
