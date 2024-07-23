# Functions are assigned as elements of a list and then called.


def func1():
    return [60, 98, 83]


def func2():
    return True


def func3():
    return {'ocgoe': 76, 'umptw': 6, 'etaxi': 66}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (20, 42, 57)


b = ["Hello"]
b[0] = func4

f = b[0]()
