# A new list is created as a slice of another one containing functions.


def func1():
    return (59, 72, 50)


def func2():
    return 98.32


def func3():
    return 2


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
