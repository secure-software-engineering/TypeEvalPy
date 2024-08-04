# A new list is created as a slice of another one containing functions.


def func1():
    return 75


def func2():
    return [59, 73, 80]


def func3():
    return 93.68


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
