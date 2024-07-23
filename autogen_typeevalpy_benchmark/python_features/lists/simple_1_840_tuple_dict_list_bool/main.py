# Functions are assigned as elements of a list and then called.


def func1():
    return (22, 17, 90)


def func2():
    return {'sxird': 41, 'kvpvr': 19, 'nqojn': 92}


def func3():
    return [40, 62, 90]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
