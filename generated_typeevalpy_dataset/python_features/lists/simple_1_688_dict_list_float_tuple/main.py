# Functions are assigned as elements of a list and then called.


def func1():
    return {'etaxg': 2, 'gitek': 2, 'lzffu': 97}


def func2():
    return [88, 41, 42]


def func3():
    return 38.74


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (43, 98, 95)


b = ["Hello"]
b[0] = func4

f = b[0]()
