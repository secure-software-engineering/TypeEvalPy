# A new list is created as a slice of another one containing functions.


def func1():
    return 'icgjg'


def func2():
    return 66


def func3():
    return (60, 5, 31)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
