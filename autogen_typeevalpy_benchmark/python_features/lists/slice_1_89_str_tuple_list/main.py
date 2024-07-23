# A new list is created as a slice of another one containing functions.


def func1():
    return 'mxfum'


def func2():
    return (37, 72, 87)


def func3():
    return [90, 46, 30]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
