# A new list is created as a slice of another one containing functions.


def func1():
    return (17, 71, 23)


def func2():
    return 'wtorj'


def func3():
    return 76.99


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
