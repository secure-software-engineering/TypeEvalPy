# Functions are assigned as elements of a list and then called.


def func1():
    return (5, 86, 33)


def func2():
    return [35, 27, 36]


def func3():
    return 6.05


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'tvzvv': 63, 'xyzfk': 25, 'mfmbv': 48}


b = ["Hello"]
b[0] = func4

f = b[0]()
