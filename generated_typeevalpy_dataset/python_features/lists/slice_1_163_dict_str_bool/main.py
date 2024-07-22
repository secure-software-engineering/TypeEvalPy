# A new list is created as a slice of another one containing functions.


def func1():
    return {'sffsx': 43, 'pipzz': 48, 'uxxgk': 33}


def func2():
    return 'atmfu'


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
