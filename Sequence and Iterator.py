# sequence and iterator


def infinite():
    """
    A generator function that yields an infinite sequence of natural numbers starting from n =1

    Returns:
        int: The next natural number in the sequence.
    """
    n = 1
    while True:
        yield n
        n += 1


num = infinite()
print(next(num))  # 1
print(next(num))  # 2
