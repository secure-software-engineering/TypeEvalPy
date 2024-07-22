# A new list is created as a slice of another one containing functions.


def func1():
    return (69, 58, 82)


def func2():
    return 52.97


def func3():
    return [100, 79, 49]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
