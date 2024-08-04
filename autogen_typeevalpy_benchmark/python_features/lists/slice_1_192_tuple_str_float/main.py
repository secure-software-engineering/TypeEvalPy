# A new list is created as a slice of another one containing functions.


def func1():
    return (56, 19, 48)


def func2():
    return 'fjkpy'


def func3():
    return 54.2


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
