# A new list is created as a slice of another one containing functions.


def func1():
    return 71.59


def func2():
    return (77, 53, 23)


def func3():
    return [79, 88, 32]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
