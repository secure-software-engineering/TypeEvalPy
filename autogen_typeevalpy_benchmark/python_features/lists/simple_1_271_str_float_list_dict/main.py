# Functions are assigned as elements of a list and then called.


def func1():
    return 'dzpmr'


def func2():
    return 57.57


def func3():
    return [92, 82, 74]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'nytmy': 52, 'dkumz': 4, 'qqnke': 82}


b = ["Hello"]
b[0] = func4

f = b[0]()
