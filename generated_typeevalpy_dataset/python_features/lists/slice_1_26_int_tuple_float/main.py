# A new list is created as a slice of another one containing functions.


def func1():
    return 58


def func2():
    return (79, 20, 33)


def func3():
    return 96.59


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
