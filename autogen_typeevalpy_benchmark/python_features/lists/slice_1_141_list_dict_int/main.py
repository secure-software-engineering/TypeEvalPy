# A new list is created as a slice of another one containing functions.


def func1():
    return [75, 74, 80]


def func2():
    return {'hjgbx': 50, 'nxjid': 3, 'hpmfw': 8}


def func3():
    return 24


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
