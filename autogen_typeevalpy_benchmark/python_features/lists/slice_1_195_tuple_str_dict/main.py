# A new list is created as a slice of another one containing functions.


def func1():
    return (10, 37, 64)


def func2():
    return 'xvteo'


def func3():
    return {'hywtn': 90, 'vhdyl': 84, 'brffk': 10}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
