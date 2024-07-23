# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return {'rhkhd': 16, 'omfwh': 72, 'xwscu': 17}


def func3():
    return 'zkdla'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
