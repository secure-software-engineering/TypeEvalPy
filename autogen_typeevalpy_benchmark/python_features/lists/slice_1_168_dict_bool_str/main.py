# A new list is created as a slice of another one containing functions.


def func1():
    return {'mbgho': 25, 'lwwjv': 74, 'pfxdp': 21}


def func2():
    return True


def func3():
    return 'rtojp'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
