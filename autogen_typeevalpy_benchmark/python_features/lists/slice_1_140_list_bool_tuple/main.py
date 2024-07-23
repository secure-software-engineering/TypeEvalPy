# A new list is created as a slice of another one containing functions.


def func1():
    return [36, 37, 5]


def func2():
    return True


def func3():
    return (18, 72, 62)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
