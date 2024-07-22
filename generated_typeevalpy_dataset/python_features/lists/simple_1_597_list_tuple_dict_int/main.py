# Functions are assigned as elements of a list and then called.


def func1():
    return [24, 10, 74]


def func2():
    return (22, 72, 66)


def func3():
    return {'uyxmz': 62, 'oacdy': 51, 'vtzty': 49}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 52


b = ["Hello"]
b[0] = func4

f = b[0]()
