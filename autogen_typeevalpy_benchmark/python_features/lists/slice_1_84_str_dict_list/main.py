# A new list is created as a slice of another one containing functions.


def func1():
    return 'pzomr'


def func2():
    return {'fpmky': 41, 'ldmkk': 33, 'horcl': 52}


def func3():
    return [92, 65, 49]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
