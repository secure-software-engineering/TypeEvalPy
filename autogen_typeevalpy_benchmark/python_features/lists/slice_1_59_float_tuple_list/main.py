# A new list is created as a slice of another one containing functions.


def func1():
    return 18.69


def func2():
    return (90, 60, 100)


def func3():
    return [83, 23, 9]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
