# A new list is created as a slice of another one containing functions.


def func1():
    return {'plgml': 75, 'gqdym': 95, 'hearp': 87}


def func2():
    return 'miilf'


def func3():
    return 2


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
