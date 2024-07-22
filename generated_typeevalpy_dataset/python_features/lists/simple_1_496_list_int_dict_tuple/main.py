# Functions are assigned as elements of a list and then called.


def func1():
    return [64, 7, 28]


def func2():
    return 97


def func3():
    return {'bjsth': 51, 'brnxs': 41, 'jxsrq': 29}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (37, 33, 67)


b = ["Hello"]
b[0] = func4

f = b[0]()
