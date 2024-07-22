# A new list is created as a slice of another one containing functions.


def func1():
    return [26, 88, 61]


def func2():
    return {'hbign': 64, 'bgupn': 87, 'ikyon': 100}


def func3():
    return 12


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
