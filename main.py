def decor(func):
  def inner(*args):
    print("-" * 15)
    func(*args)
    print("-" * 15)
  return inner

def ordinary():
  print("I'm ordinary")

ordinary()

decorated = decor(ordinary)
decorated()
decor(ordinary)()

@decor
def congrats(name):
  print("Hello,", name)

congrats("Sam")