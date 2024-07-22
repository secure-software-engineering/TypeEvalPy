# Functions are assigned as elements of a list and then called.


def func1():
    return (75, 66, 64)


def func2():
    return 'dwwjn'


def func3():
    return 12


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'lcimd': 56, 'mouky': 46, 'canfx': 61}


b = ["Hello"]
b[0] = func4

f = b[0]()
