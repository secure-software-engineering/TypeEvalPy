# Functions are assigned as elements of a list and then called.


def func1():
    return {'zqhjl': 91, 'orije': 94, 'cncjk': 99}


def func2():
    return (17, 78, 63)


def func3():
    return [28, 62, 100]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 13.38


b = ["Hello"]
b[0] = func4

f = b[0]()
