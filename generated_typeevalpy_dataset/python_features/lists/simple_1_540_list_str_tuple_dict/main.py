# Functions are assigned as elements of a list and then called.


def func1():
    return [14, 53, 79]


def func2():
    return 'nihln'


def func3():
    return (90, 29, 6)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'mpuvg': 24, 'kjidx': 5, 'eaxxp': 60}


b = ["Hello"]
b[0] = func4

f = b[0]()
