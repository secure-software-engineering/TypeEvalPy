# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'hblml': 81, 'auzmo': 61, 'rqwwh': 30}


def func3():
    return 3


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [58, 38, 70]


b = ["Hello"]
b[0] = func4

f = b[0]()
