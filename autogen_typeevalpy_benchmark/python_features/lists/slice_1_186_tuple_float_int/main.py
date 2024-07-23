# A new list is created as a slice of another one containing functions.


def func1():
    return (57, 40, 36)


def func2():
    return 53.58


def func3():
    return 97


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
