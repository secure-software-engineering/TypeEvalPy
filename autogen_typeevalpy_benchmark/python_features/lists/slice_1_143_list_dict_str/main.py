# A new list is created as a slice of another one containing functions.


def func1():
    return [17, 29, 2]


def func2():
    return {'mvtrq': 40, 'drspk': 18, 'tqrxh': 88}


def func3():
    return 'uxnil'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
