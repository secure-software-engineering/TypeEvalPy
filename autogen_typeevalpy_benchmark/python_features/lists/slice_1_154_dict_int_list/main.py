# A new list is created as a slice of another one containing functions.


def func1():
    return {'nerwm': 17, 'xpfjq': 32, 'eeogx': 89}


def func2():
    return 20


def func3():
    return [70, 76, 2]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
