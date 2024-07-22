# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return 25.62


def func3():
    return (79, 72, 73)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
