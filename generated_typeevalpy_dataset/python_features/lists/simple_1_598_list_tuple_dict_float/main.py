# Functions are assigned as elements of a list and then called.


def func1():
    return [74, 65, 30]


def func2():
    return (51, 62, 56)


def func3():
    return {'nqjad': 34, 'tjpdf': 52, 'tedgu': 95}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 36.58


b = ["Hello"]
b[0] = func4

f = b[0]()
