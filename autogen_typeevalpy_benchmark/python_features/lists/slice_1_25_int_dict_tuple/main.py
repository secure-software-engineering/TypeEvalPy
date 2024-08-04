# A new list is created as a slice of another one containing functions.


def func1():
    return 45


def func2():
    return {'eoofm': 58, 'sqfuk': 57, 'vhzlk': 28}


def func3():
    return (4, 12, 34)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
