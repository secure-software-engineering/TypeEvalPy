# A new list is created as a slice of another one containing functions.


def func1():
    return 39.84


def func2():
    return (89, 43, 85)


def func3():
    return [17, 100, 28]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
