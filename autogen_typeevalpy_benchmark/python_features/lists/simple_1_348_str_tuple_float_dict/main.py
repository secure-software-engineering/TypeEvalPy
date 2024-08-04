# Functions are assigned as elements of a list and then called.


def func1():
    return 'mswcf'


def func2():
    return (5, 82, 6)


def func3():
    return 19.32


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'oygzn': 5, 'mzmss': 91, 'wxjqy': 21}


b = ["Hello"]
b[0] = func4

f = b[0]()
