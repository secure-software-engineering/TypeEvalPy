# A new list is created as a slice of another one containing functions.


def func1():
    return [45, 49, 63]


def func2():
    return 13.98


def func3():
    return (99, 94, 45)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
