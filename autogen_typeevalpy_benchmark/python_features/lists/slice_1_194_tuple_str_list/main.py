# A new list is created as a slice of another one containing functions.


def func1():
    return (62, 10, 51)


def func2():
    return 'sgsye'


def func3():
    return [59, 49, 95]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
