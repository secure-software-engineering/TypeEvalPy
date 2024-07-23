# Functions are assigned as elements of a list and then called.


def func1():
    return {'hzzgo': 53, 'edqnp': 83, 'znikn': 95}


def func2():
    return [25, 1, 16]


def func3():
    return 'eudgq'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 21.38


b = ["Hello"]
b[0] = func4

f = b[0]()
