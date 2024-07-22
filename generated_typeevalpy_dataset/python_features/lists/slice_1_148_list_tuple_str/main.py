# A new list is created as a slice of another one containing functions.


def func1():
    return [36, 2, 62]


def func2():
    return (65, 1, 88)


def func3():
    return 'lachf'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
