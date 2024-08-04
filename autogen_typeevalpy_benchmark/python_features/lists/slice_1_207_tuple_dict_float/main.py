# A new list is created as a slice of another one containing functions.


def func1():
    return (11, 39, 10)


def func2():
    return {'evbta': 54, 'mmwoe': 16, 'gyqiz': 15}


def func3():
    return 34.09


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
