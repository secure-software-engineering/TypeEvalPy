# A new list is created as a slice of another one containing functions.


def func1():
    return 'plehz'


def func2():
    return 34.54


def func3():
    return {'dvlyg': 81, 'zucub': 6, 'bgqim': 43}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
