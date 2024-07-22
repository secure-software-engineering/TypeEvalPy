# A new list is created as a slice of another one containing functions.


def func1():
    return (77, 2, 70)


def func2():
    return 3


def func3():
    return 81.95


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
