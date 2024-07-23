# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return 76.19


def func3():
    return {'zlwlb': 46, 'ttpmc': 31, 'npruu': 17}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
