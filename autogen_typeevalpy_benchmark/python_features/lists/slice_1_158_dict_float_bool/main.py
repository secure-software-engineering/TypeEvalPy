# A new list is created as a slice of another one containing functions.


def func1():
    return {'omjxi': 39, 'sscqp': 90, 'oqntt': 7}


def func2():
    return 90.51


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
