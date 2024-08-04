# Functions are assigned as elements of a list and then called.


def func1():
    return {'jnyqe': 66, 'bgwbu': 76, 'rluqg': 66}


def func2():
    return [30, 1, 16]


def func3():
    return 52.58


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'vvxas'


b = ["Hello"]
b[0] = func4

f = b[0]()
