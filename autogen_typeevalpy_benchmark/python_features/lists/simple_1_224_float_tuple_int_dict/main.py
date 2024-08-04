# Functions are assigned as elements of a list and then called.


def func1():
    return 30.96


def func2():
    return (69, 62, 16)


def func3():
    return 100


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'iirzf': 57, 'qbvnw': 95, 'athcx': 29}


b = ["Hello"]
b[0] = func4

f = b[0]()
