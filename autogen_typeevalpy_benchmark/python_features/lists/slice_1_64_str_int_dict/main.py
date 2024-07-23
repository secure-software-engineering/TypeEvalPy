# A new list is created as a slice of another one containing functions.


def func1():
    return 'oyunp'


def func2():
    return 45


def func3():
    return {'eewcd': 88, 'vbrcq': 29, 'wucbx': 3}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
