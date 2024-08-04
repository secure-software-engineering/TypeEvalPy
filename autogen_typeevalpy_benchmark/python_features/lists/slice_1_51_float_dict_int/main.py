# A new list is created as a slice of another one containing functions.


def func1():
    return 22.57


def func2():
    return {'ccesd': 90, 'upiyf': 23, 'dzdwk': 85}


def func3():
    return 6


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
