# A new list is created as a slice of another one containing functions.


def func1():
    return (79, 25, 28)


def func2():
    return False


def func3():
    return 30.89


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
