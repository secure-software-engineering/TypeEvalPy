# A new list is created as a slice of another one containing functions.


def func1():
    return 6


def func2():
    return {'arpcf': 28, 'khjpg': 38, 'tdieq': 90}


def func3():
    return 95.53


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
