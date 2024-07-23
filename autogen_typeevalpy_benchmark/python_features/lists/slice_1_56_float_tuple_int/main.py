# A new list is created as a slice of another one containing functions.


def func1():
    return 44.43


def func2():
    return (66, 51, 82)


def func3():
    return 30


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
