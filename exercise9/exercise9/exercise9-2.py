from functools import reduce


def ex2(list1):
    result = list(filter((lambda x: x % 2), list1))
    print(result)
    result = reduce((lambda x, y: x + y), result)
    print(result)


list1 = list(range(100))

ex2(list1)
