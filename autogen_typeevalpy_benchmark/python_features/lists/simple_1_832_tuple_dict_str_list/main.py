# Functions are assigned as elements of a list and then called.


def func1():
    return (74, 21, 8)


def func2():
    return {'yugos': 9, 'kjxmc': 84, 'iymoe': 30}


def func3():
    return 'ovbkm'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [87, 85, 83]


b = ["Hello"]
b[0] = func4

f = b[0]()
