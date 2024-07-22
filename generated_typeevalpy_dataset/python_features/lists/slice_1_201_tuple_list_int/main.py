# A new list is created as a slice of another one containing functions.


def func1():
    return (27, 89, 39)


def func2():
    return [46, 66, 19]


def func3():
    return 36


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
