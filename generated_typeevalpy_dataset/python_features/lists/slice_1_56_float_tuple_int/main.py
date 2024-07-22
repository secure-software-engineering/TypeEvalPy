# A new list is created as a slice of another one containing functions.


def func1():
    return 71.49


def func2():
    return (62, 56, 45)


def func3():
    return 46


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
