# Functions are assigned as elements of a list and then called.


def func1():
    return {'mrloe': 89, 'qpggu': 71, 'qzgfm': 40}


def func2():
    return 43


def func3():
    return 'lvgps'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 73.78


b = ["Hello"]
b[0] = func4

f = b[0]()
