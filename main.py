def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

generator = PowTwoGen(3)
print(next(generator))
print(next(generator))
print(next(generator))

squares_generator = (i * i for i in range(3))
print(next(squares_generator))
print(next(squares_generator))
print(next(squares_generator))