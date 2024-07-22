# A new list is created as a slice of another one containing functions.


def func1():
    return 86.18


def func2():
    return [21, 69, 100]


def func3():
    return {'gevbm': 44, 'bcilw': 20, 'wfkab': 98}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
