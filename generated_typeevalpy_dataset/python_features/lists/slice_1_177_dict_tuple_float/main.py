# A new list is created as a slice of another one containing functions.


def func1():
    return {'mhlxk': 46, 'jkmeu': 80, 'idukd': 69}


def func2():
    return (42, 82, 55)


def func3():
    return 14.3


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
