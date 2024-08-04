# A new list is created as a slice of another one containing functions.


def func1():
    return (30, 87, 93)


def func2():
    return 10


def func3():
    return {'ryrzr': 4, 'pulib': 10, 'npdqb': 5}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
