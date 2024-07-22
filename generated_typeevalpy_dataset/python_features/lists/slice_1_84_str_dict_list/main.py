# A new list is created as a slice of another one containing functions.


def func1():
    return 'ctudp'


def func2():
    return {'yzayj': 70, 'khuan': 92, 'sclsd': 100}


def func3():
    return [62, 78, 32]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
