# A new list is created as a slice of another one containing functions.


def func1():
    return 44.02


def func2():
    return True


def func3():
    return {'oadnp': 25, 'fegra': 52, 'kewmd': 76}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
