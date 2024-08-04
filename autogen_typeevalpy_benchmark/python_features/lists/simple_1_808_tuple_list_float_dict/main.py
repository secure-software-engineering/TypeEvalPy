# Functions are assigned as elements of a list and then called.


def func1():
    return (6, 7, 19)


def func2():
    return [93, 96, 7]


def func3():
    return 20.04


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'gfxmo': 79, 'aacxv': 44, 'weniw': 48}


b = ["Hello"]
b[0] = func4

f = b[0]()
