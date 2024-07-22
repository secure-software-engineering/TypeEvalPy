# Functions are assigned as elements of a list and then called.


def func1():
    return (98, 55, 21)


def func2():
    return 'mjpgs'


def func3():
    return [88, 52, 7]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'asxvz': 8, 'hlurb': 99, 'yycfm': 82}


b = ["Hello"]
b[0] = func4

f = b[0]()
