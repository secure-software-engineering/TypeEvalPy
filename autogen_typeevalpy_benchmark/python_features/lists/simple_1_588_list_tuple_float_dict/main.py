# Functions are assigned as elements of a list and then called.


def func1():
    return [51, 46, 11]


def func2():
    return (96, 55, 49)


def func3():
    return 13.1


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rcsmj': 36, 'dgthv': 75, 'wysbi': 19}


b = ["Hello"]
b[0] = func4

f = b[0]()
