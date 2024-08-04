# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return 8


def func3():
    return [70, 49, 53]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
