# A new list is created as a slice of another one containing functions.


def func1():
    return (33, 19, 50)


def func2():
    return 'tpefx'


def func3():
    return [33, 39, 72]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
