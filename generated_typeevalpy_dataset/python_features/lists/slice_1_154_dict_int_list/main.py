# A new list is created as a slice of another one containing functions.


def func1():
    return {'yeqrn': 24, 'czxro': 25, 'rlarl': 85}


def func2():
    return 13


def func3():
    return [90, 33, 93]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
