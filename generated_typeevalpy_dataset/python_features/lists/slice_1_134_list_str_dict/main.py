# A new list is created as a slice of another one containing functions.


def func1():
    return [35, 69, 80]


def func2():
    return 'jdtxl'


def func3():
    return {'nccgj': 22, 'ldlcp': 16, 'nvzhe': 59}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
