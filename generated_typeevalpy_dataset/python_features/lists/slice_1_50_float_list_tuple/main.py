# A new list is created as a slice of another one containing functions.


def func1():
    return 98.1


def func2():
    return [17, 8, 22]


def func3():
    return (69, 64, 82)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
