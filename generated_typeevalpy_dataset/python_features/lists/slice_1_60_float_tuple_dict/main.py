# A new list is created as a slice of another one containing functions.


def func1():
    return 65.12


def func2():
    return (9, 8, 6)


def func3():
    return {'kpxdk': 29, 'tuwxd': 25, 'shhuv': 90}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
