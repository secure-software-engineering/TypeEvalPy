# A new list is created as a slice of another one containing functions.


def func1():
    return 92.77


def func2():
    return False


def func3():
    return (14, 39, 53)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
