# A new list is created as a slice of another one containing functions.


def func1():
    return {'efpeh': 34, 'ikpqt': 10, 'dvwec': 87}


def func2():
    return 64.97


def func3():
    return 'xxewh'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
