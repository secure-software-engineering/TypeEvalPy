# A new list is created as a slice of another one containing functions.


def func1():
    return [77, 71, 73]


def func2():
    return 'vfhds'


def func3():
    return (9, 64, 8)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
