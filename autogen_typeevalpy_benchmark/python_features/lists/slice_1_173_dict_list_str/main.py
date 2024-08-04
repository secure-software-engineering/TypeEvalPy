# A new list is created as a slice of another one containing functions.


def func1():
    return {'iazto': 57, 'dafaw': 52, 'qdpsr': 44}


def func2():
    return [80, 43, 38]


def func3():
    return 'whaon'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
