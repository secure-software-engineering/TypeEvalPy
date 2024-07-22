# A new list is created as a slice of another one containing functions.


def func1():
    return [78, 92, 27]


def func2():
    return 'yawvb'


def func3():
    return (90, 23, 49)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
