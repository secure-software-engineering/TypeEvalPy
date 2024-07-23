# A new list is created as a slice of another one containing functions.


def func1():
    return (6, 100, 8)


def func2():
    return True


def func3():
    return 12


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
