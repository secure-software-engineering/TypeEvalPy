# A new list is created as a slice of another one containing functions.


def func1():
    return [2, 88, 94]


def func2():
    return 'bgwoy'


def func3():
    return 13


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
