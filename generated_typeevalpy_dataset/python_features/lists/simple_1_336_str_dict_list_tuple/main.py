# Functions are assigned as elements of a list and then called.


def func1():
    return 'cyxjo'


def func2():
    return {'paeum': 11, 'hnkwx': 1, 'qrltl': 56}


def func3():
    return [38, 8, 12]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (22, 76, 22)


b = ["Hello"]
b[0] = func4

f = b[0]()
