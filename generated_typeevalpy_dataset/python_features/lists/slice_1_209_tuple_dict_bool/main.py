# A new list is created as a slice of another one containing functions.


def func1():
    return (33, 67, 57)


def func2():
    return {'revtm': 95, 'hymnu': 2, 'pmobo': 33}


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
