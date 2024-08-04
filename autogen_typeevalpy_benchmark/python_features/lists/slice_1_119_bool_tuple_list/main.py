# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return (95, 85, 75)


def func3():
    return [85, 33, 16]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
