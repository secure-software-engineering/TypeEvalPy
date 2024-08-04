# A new list is created as a slice of another one containing functions.


def func1():
    return [91, 60, 44]


def func2():
    return (88, 71, 77)


def func3():
    return 47.9


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
