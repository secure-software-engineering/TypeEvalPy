# A new list is created as a slice of another one containing functions.


def func1():
    return (16, 6, 2)


def func2():
    return [61, 30, 22]


def func3():
    return 16.53


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
