# A new list is created as a slice of another one containing functions.


def func1():
    return (74, 1, 10)


def func2():
    return 'byhsu'


def func3():
    return 61


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
