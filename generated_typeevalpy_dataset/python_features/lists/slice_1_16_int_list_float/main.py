# A new list is created as a slice of another one containing functions.


def func1():
    return 96


def func2():
    return [88, 94, 36]


def func3():
    return 80.66


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
