# A new list is created as a slice of another one containing functions.


def func1():
    return [36, 51, 80]


def func2():
    return (97, 67, 91)


def func3():
    return 56


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
