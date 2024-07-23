# A new list is created as a slice of another one containing functions.


def func1():
    return 36


def func2():
    return (24, 72, 32)


def func3():
    return [31, 25, 99]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
