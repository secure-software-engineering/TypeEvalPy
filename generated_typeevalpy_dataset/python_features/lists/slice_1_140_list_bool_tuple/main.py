# A new list is created as a slice of another one containing functions.


def func1():
    return [15, 90, 87]


def func2():
    return False


def func3():
    return (24, 69, 10)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
