# A new list is created as a slice of another one containing functions.


def func1():
    return [47, 45, 81]


def func2():
    return {'nainp': 61, 'pchxe': 60, 'flxfe': 52}


def func3():
    return 26.59


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
