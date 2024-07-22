# A new list is created as a slice of another one containing functions.


def func1():
    return [32, 79, 86]


def func2():
    return 68


def func3():
    return (85, 95, 15)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
