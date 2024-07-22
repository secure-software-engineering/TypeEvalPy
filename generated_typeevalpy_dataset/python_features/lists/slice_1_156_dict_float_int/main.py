# A new list is created as a slice of another one containing functions.


def func1():
    return {'uxunt': 13, 'sicdn': 50, 'ajdlt': 73}


def func2():
    return 52.35


def func3():
    return 67


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
