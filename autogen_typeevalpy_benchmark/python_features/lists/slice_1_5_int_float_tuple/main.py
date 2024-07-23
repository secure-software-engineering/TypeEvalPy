# A new list is created as a slice of another one containing functions.


def func1():
    return 25


def func2():
    return 36.86


def func3():
    return (15, 31, 40)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
