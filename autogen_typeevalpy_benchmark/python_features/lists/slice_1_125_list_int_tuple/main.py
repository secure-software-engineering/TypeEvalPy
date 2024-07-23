# A new list is created as a slice of another one containing functions.


def func1():
    return [20, 15, 44]


def func2():
    return 38


def func3():
    return (20, 94, 74)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
