# A new list is created as a slice of another one containing functions.


def func1():
    return 'vtuno'


def func2():
    return {'nrcav': 100, 'taxha': 86, 'mmnku': 26}


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
