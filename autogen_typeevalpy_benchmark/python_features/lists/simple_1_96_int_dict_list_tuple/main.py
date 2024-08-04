# Functions are assigned as elements of a list and then called.


def func1():
    return 63


def func2():
    return {'wyqph': 17, 'lzder': 96, 'twufn': 49}


def func3():
    return [45, 55, 16]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (73, 61, 69)


b = ["Hello"]
b[0] = func4

f = b[0]()
