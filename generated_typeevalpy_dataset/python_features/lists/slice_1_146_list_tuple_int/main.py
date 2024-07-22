# A new list is created as a slice of another one containing functions.


def func1():
    return [55, 21, 89]


def func2():
    return (39, 73, 7)


def func3():
    return 23


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
