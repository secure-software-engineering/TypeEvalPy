# A new list is created as a slice of another one containing functions.


def func1():
    return [89, 17, 35]


def func2():
    return 'gdcpv'


def func3():
    return {'iuadt': 57, 'rpngy': 57, 'qetgj': 4}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
