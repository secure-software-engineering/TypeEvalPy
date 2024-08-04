# A new list is created as a slice of another one containing functions.


def func1():
    return False


def func2():
    return (12, 26, 7)


def func3():
    return {'midpq': 17, 'fpeaj': 85, 'mwaop': 20}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
