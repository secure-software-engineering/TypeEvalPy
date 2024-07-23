# A new list is created as a slice of another one containing functions.


def func1():
    return {'iokre': 42, 'ikezr': 21, 'tndxo': 54}


def func2():
    return False


def func3():
    return 62.96


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
