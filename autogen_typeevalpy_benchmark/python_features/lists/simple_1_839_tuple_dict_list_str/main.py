# Functions are assigned as elements of a list and then called.


def func1():
    return (25, 93, 20)


def func2():
    return {'hvdan': 5, 'pybez': 14, 'pflzz': 7}


def func3():
    return [20, 86, 32]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'odrrp'


b = ["Hello"]
b[0] = func4

f = b[0]()
