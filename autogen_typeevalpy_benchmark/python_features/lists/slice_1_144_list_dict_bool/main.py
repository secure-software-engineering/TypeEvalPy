# A new list is created as a slice of another one containing functions.


def func1():
    return [21, 37, 49]


def func2():
    return {'fbfnm': 34, 'ypicb': 99, 'fjtpo': 90}


def func3():
    return True


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
