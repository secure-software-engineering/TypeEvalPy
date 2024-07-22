# A new list is created as a slice of another one containing functions.


def func1():
    return 25.73


def func2():
    return [50, 98, 62]


def func3():
    return 55


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
