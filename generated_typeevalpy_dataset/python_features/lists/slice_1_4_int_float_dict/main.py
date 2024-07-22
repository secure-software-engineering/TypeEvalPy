# A new list is created as a slice of another one containing functions.


def func1():
    return 88


def func2():
    return 62.17


def func3():
    return {'lvloy': 39, 'ooccm': 41, 'evhjj': 91}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
