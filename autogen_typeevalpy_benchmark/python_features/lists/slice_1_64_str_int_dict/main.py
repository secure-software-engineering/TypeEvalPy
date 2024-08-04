# A new list is created as a slice of another one containing functions.


def func1():
    return 'njvwr'


def func2():
    return 1


def func3():
    return {'pdsya': 18, 'iqzja': 94, 'fdvvt': 89}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
