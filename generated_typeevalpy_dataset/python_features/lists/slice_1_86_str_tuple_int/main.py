# A new list is created as a slice of another one containing functions.


def func1():
    return 'ytbex'


def func2():
    return (10, 46, 84)


def func3():
    return 91


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
