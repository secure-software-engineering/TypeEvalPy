# A new list is created as a slice of another one containing functions.


def func1():
    return [30, 55, 60]


def func2():
    return {'vroji': 81, 'slnqq': 60, 'oarng': 86}


def func3():
    return (15, 62, 78)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
