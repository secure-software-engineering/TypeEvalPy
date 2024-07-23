# A new list is created as a slice of another one containing functions.


def func1():
    return (47, 8, 44)


def func2():
    return {'lntbj': 14, 'mjvil': 94, 'jzexb': 39}


def func3():
    return 63


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
