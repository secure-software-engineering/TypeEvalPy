# Functions are assigned as elements of a list and then called.


def func1():
    return (41, 37, 8)


def func2():
    return {'dogop': 15, 'ccjrn': 12, 'wubgl': 35}


def func3():
    return 71


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 72.56


b = ["Hello"]
b[0] = func4

f = b[0]()
