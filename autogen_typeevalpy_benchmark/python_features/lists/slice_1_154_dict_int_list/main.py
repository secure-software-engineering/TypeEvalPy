# A new list is created as a slice of another one containing functions.


def func1():
    return {'yeejn': 50, 'hccjv': 14, 'idsab': 3}


def func2():
    return 4


def func3():
    return [12, 48, 61]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
