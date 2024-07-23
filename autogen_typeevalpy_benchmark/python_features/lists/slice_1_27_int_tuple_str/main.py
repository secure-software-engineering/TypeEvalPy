# A new list is created as a slice of another one containing functions.


def func1():
    return 51


def func2():
    return (61, 90, 78)


def func3():
    return 'ejgeg'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
