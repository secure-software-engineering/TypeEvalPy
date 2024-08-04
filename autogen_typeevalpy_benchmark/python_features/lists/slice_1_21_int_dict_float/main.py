# A new list is created as a slice of another one containing functions.


def func1():
    return 16


def func2():
    return {'uuxyp': 56, 'kdfum': 63, 'vzqog': 67}


def func3():
    return 42.0


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
