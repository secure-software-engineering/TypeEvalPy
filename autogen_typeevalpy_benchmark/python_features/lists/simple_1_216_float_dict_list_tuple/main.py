# Functions are assigned as elements of a list and then called.


def func1():
    return 99.06


def func2():
    return {'xxqzu': 83, 'ueeir': 7, 'lamnu': 68}


def func3():
    return [28, 57, 35]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (29, 19, 94)


b = ["Hello"]
b[0] = func4

f = b[0]()
