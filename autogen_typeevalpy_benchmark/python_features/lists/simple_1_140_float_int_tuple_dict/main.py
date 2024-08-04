# Functions are assigned as elements of a list and then called.


def func1():
    return 3.12


def func2():
    return 14


def func3():
    return (19, 41, 78)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'onnft': 85, 'szyro': 24, 'rqbiy': 94}


b = ["Hello"]
b[0] = func4

f = b[0]()
