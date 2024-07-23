# A new list is created as a slice of another one containing functions.


def func1():
    return 96


def func2():
    return {'usjfm': 35, 'uscvj': 12, 'dxcpb': 75}


def func3():
    return 'fylll'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
