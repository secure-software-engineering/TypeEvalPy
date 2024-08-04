# A new list is created as a slice of another one containing functions.


def func1():
    return {'zyozc': 3, 'dhqlf': 33, 'qluog': 100}


def func2():
    return 45.39


def func3():
    return (6, 15, 32)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
