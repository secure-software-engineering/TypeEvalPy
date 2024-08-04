# A new list is created as a slice of another one containing functions.


def func1():
    return [54, 31, 93]


def func2():
    return 1


def func3():
    return 94.06


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
