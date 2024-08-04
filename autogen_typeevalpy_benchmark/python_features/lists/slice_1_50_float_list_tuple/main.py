# A new list is created as a slice of another one containing functions.


def func1():
    return 63.8


def func2():
    return [13, 37, 24]


def func3():
    return (60, 5, 76)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
