# A new list is created as a slice of another one containing functions.


def func1():
    return (62, 93, 83)


def func2():
    return [33, 8, 33]


def func3():
    return 'qxauy'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
