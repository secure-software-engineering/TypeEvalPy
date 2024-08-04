# A new list is created as a slice of another one containing functions.


def func1():
    return 'qzrds'


def func2():
    return {'kpeee': 36, 'quqja': 80, 'ynxhl': 75}


def func3():
    return [42, 24, 91]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
