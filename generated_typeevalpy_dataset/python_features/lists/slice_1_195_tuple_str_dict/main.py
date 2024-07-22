# A new list is created as a slice of another one containing functions.


def func1():
    return (71, 51, 16)


def func2():
    return 'gjygf'


def func3():
    return {'fxsbi': 44, 'rrtxm': 65, 'dvyxx': 30}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
