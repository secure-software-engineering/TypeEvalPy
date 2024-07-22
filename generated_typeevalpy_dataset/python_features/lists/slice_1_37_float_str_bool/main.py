# A new list is created as a slice of another one containing functions.


def func1():
    return 13.76


def func2():
    return 'oesdb'


def func3():
    return True


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
