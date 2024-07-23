# A new list is created as a slice of another one containing functions.


def func1():
    return 'teygu'


def func2():
    return 38.61


def func3():
    return (65, 35, 22)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
