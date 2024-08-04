# A new list is created as a slice of another one containing functions.


def func1():
    return (63, 61, 84)


def func2():
    return 7


def func3():
    return [32, 71, 77]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
