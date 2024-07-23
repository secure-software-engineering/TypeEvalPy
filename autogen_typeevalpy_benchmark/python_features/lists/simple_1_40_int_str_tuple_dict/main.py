# Functions are assigned as elements of a list and then called.


def func1():
    return 67


def func2():
    return 'rcxhf'


def func3():
    return (31, 74, 92)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'kguia': 15, 'ybsut': 95, 'pxjnq': 37}


b = ["Hello"]
b[0] = func4

f = b[0]()
