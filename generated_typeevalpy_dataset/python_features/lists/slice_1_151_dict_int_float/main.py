# A new list is created as a slice of another one containing functions.


def func1():
    return {'wfpoc': 87, 'rydwk': 68, 'yvrcc': 25}


def func2():
    return 55


def func3():
    return 8.73


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
