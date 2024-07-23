# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return {'skwcz': 68, 'vsmnh': 51, 'jschr': 28}


def func3():
    return [55, 71, 74]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 41.9


b = ["Hello"]
b[0] = func4

f = b[0]()
