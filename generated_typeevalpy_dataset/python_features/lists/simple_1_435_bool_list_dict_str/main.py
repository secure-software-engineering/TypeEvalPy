# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return [47, 66, 29]


def func3():
    return {'qxpuu': 1, 'jzkwn': 55, 'okxcu': 48}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'osjwp'


b = ["Hello"]
b[0] = func4

f = b[0]()
