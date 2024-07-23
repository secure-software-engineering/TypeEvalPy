# A new list is created as a slice of another one containing functions.


def func1():
    return 'zartq'


def func2():
    return 66.02


def func3():
    return {'nbaew': 77, 'muins': 77, 'oykeq': 10}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
