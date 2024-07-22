# Functions are assigned as elements of a list and then called.


def func1():
    return [87, 8, 66]


def func2():
    return (49, 32, 55)


def func3():
    return 'zwlhi'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'xvyfc': 35, 'ceftb': 73, 'tllgq': 87}


b = ["Hello"]
b[0] = func4

f = b[0]()
