from multipledispatch import dispatch


@dispatch(int, int)
def product(first, second):
    RESULT = first * second
    print(RESULT)


@dispatch(int, int, int)
def product(first, second, third):
    RESULT = first * second * third
    print(RESULT)


@dispatch(float, float, float)
def product(first, second, third):
    RESULT = first * second * third
    print(RESULT)


product(5, 6)

product(2, 4, 6)

product(3.2, 5.2, 2.0)
