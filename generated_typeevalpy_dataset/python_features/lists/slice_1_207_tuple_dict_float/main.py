# A new list is created as a slice of another one containing functions.


def func1():
    return (99, 13, 8)


def func2():
    return {'gpmzg': 88, 'sburx': 53, 'mbpxl': 91}


def func3():
    return 19.63


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
