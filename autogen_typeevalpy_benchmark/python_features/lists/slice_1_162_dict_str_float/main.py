# A new list is created as a slice of another one containing functions.


def func1():
    return {'veimh': 72, 'zaddd': 52, 'vnlqt': 56}


def func2():
    return 'wwauc'


def func3():
    return 75.61


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
