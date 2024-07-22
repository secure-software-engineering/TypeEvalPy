# A new list is created as a slice of another one containing functions.


def func1():
    return {'dxqpr': 31, 'srurp': 92, 'favwt': 68}


def func2():
    return [78, 55, 68]


def func3():
    return 86.0


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
