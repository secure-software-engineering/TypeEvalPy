# A new list is created as a slice of another one containing functions.


def func1():
    return 59.56


def func2():
    return 76


def func3():
    return (67, 43, 74)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
