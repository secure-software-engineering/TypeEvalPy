# A new list is created as a slice of another one containing functions.


def func1():
    return (87, 32, 58)


def func2():
    return [71, 55, 16]


def func3():
    return 24


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
