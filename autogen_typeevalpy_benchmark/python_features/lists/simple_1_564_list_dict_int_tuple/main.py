# Functions are assigned as elements of a list and then called.


def func1():
    return [99, 94, 65]


def func2():
    return {'jktns': 86, 'mkmzl': 53, 'dyofv': 62}


def func3():
    return 87


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (56, 18, 20)


b = ["Hello"]
b[0] = func4

f = b[0]()
