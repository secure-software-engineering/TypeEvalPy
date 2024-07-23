# A new list is created as a slice of another one containing functions.


def func1():
    return [6, 87, 2]


def func2():
    return (98, 89, 5)


def func3():
    return 60


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
