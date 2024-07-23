# A new list is created as a slice of another one containing functions.


def func1():
    return (16, 34, 60)


def func2():
    return 12.23


def func3():
    return [50, 16, 52]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
