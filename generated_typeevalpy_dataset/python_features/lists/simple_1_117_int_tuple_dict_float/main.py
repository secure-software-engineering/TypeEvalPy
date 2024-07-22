# Functions are assigned as elements of a list and then called.


def func1():
    return 1


def func2():
    return (53, 91, 38)


def func3():
    return {'bwudx': 84, 'srtwr': 21, 'bsmsq': 37}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 61.87


b = ["Hello"]
b[0] = func4

f = b[0]()
