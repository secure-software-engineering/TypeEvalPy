# Functions are assigned as elements of a list and then called.


def func1():
    return 'gsdnn'


def func2():
    return (83, 36, 93)


def func3():
    return {'nairc': 36, 'gnsmm': 64, 'ugppg': 12}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 53.88


b = ["Hello"]
b[0] = func4

f = b[0]()
