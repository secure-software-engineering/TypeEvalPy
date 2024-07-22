# A new list is created as a slice of another one containing functions.


def func1():
    return 88.4


def func2():
    return 52


def func3():
    return (70, 59, 52)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
