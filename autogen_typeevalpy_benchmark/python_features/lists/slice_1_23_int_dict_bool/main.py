# A new list is created as a slice of another one containing functions.


def func1():
    return 47


def func2():
    return {'nwpvt': 73, 'xyocs': 10, 'rpgso': 76}


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
