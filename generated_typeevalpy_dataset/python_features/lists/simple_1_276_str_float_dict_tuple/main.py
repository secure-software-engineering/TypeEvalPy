# Functions are assigned as elements of a list and then called.


def func1():
    return 'ssamv'


def func2():
    return 23.18


def func3():
    return {'njdoe': 47, 'tkvii': 32, 'idozf': 15}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (23, 88, 91)


b = ["Hello"]
b[0] = func4

f = b[0]()
