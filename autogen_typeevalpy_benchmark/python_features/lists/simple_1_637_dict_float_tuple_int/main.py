# Functions are assigned as elements of a list and then called.


def func1():
    return {'fjqwa': 4, 'mlvgf': 15, 'yorbi': 89}


def func2():
    return 97.48


def func3():
    return (26, 27, 25)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 100


b = ["Hello"]
b[0] = func4

f = b[0]()
