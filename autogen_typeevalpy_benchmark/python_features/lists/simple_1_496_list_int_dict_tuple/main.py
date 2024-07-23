# Functions are assigned as elements of a list and then called.


def func1():
    return [46, 78, 81]


def func2():
    return 49


def func3():
    return {'lrajo': 64, 'bmqiq': 47, 'ajzkm': 98}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (68, 5, 98)


b = ["Hello"]
b[0] = func4

f = b[0]()
