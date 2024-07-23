# A new list is created as a slice of another one containing functions.


def func1():
    return 57.15


def func2():
    return [87, 9, 40]


def func3():
    return {'bclyv': 89, 'yzzwx': 37, 'qfsho': 54}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
