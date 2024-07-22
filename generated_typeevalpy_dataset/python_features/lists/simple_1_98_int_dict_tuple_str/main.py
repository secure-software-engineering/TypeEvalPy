# Functions are assigned as elements of a list and then called.


def func1():
    return 2


def func2():
    return {'bgnff': 20, 'huwle': 17, 'gfsqz': 86}


def func3():
    return (68, 71, 65)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'buadj'


b = ["Hello"]
b[0] = func4

f = b[0]()
