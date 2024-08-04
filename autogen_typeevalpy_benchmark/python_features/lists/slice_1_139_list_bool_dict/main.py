# A new list is created as a slice of another one containing functions.


def func1():
    return [61, 16, 27]


def func2():
    return True


def func3():
    return {'tkwna': 82, 'utbse': 1, 'wrkbr': 55}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
