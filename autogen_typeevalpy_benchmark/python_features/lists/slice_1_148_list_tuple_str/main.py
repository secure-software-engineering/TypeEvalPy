# A new list is created as a slice of another one containing functions.


def func1():
    return [21, 30, 46]


def func2():
    return (75, 24, 62)


def func3():
    return 'komxg'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
