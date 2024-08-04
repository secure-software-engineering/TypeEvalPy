# Functions are assigned as elements of a list and then called.


def func1():
    return [14, 78, 29]


def func2():
    return 48


def func3():
    return (72, 13, 48)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ccujv': 35, 'hbyzu': 77, 'iagoh': 41}


b = ["Hello"]
b[0] = func4

f = b[0]()
