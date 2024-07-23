# A new list is created as a slice of another one containing functions.


def func1():
    return 9


def func2():
    return {'qqssm': 89, 'kolzb': 48, 'dafhw': 79}


def func3():
    return (80, 43, 60)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
