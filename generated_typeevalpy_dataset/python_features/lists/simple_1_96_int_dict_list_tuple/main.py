# Functions are assigned as elements of a list and then called.


def func1():
    return 34


def func2():
    return {'rkkir': 76, 'njfdm': 56, 'djrfj': 49}


def func3():
    return [87, 44, 63]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (82, 88, 54)


b = ["Hello"]
b[0] = func4

f = b[0]()
