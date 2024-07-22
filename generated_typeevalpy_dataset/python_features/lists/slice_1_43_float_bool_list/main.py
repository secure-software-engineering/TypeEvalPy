# A new list is created as a slice of another one containing functions.


def func1():
    return 70.86


def func2():
    return False


def func3():
    return [35, 73, 88]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
