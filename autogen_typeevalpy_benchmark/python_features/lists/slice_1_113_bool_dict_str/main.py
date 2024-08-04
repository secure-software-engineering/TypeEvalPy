# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return {'gdoqy': 66, 'lxayb': 67, 'psmyn': 2}


def func3():
    return 'rkqrb'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
