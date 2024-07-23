# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return [25, 6, 14]


def func3():
    return (1, 90, 95)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
