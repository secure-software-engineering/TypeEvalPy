# A new list is created as a slice of another one containing functions.


def func1():
    return 29


def func2():
    return {'chfmx': 87, 'frqir': 39, 'zngao': 54}


def func3():
    return [94, 70, 95]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
