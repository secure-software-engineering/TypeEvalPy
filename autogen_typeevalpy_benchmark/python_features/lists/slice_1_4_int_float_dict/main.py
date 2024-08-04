# A new list is created as a slice of another one containing functions.


def func1():
    return 50


def func2():
    return 44.65


def func3():
    return {'faxdy': 52, 'tmobp': 95, 'rdpau': 66}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
