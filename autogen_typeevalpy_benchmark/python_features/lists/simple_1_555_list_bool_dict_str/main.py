# Functions are assigned as elements of a list and then called.


def func1():
    return [6, 83, 68]


def func2():
    return True


def func3():
    return {'cypuv': 70, 'mavha': 70, 'fenan': 64}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'iywyd'


b = ["Hello"]
b[0] = func4

f = b[0]()
