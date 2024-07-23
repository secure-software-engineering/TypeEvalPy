# A new list is created as a slice of another one containing functions.


def func1():
    return 23


def func2():
    return 4.55


def func3():
    return {'amldi': 53, 'hnjzc': 7, 'gqfut': 99}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
