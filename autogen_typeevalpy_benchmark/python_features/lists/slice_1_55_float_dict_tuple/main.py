# A new list is created as a slice of another one containing functions.


def func1():
    return 30.99


def func2():
    return {'okfla': 43, 'pjxiz': 24, 'owzqp': 53}


def func3():
    return (45, 98, 63)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
