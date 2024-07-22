# A new list is created as a slice of another one containing functions.


def func1():
    return 9


def func2():
    return 82.52


def func3():
    return [89, 78, 44]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
