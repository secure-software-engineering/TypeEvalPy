# A new list is created as a slice of another one containing functions.


def func1():
    return {'flnfr': 96, 'inixe': 65, 'qvypi': 9}


def func2():
    return 29.03


def func3():
    return True


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
