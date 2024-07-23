# A new list is created as a slice of another one containing functions.


def func1():
    return 'qwxhl'


def func2():
    return False


def func3():
    return {'rsajs': 48, 'nnzxj': 10, 'etonb': 7}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
