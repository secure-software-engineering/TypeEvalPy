# A new list is created as a slice of another one containing functions.


def func1():
    return False


def func2():
    return 43


def func3():
    return {'nrifg': 73, 'zewgg': 88, 'pfhlj': 40}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
