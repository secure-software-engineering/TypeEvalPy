# A new list is created as a slice of another one containing functions.


def func1():
    return 39.11


def func2():
    return 'prhan'


def func3():
    return {'sviwz': 13, 'qzaiz': 39, 'gpqwo': 72}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
