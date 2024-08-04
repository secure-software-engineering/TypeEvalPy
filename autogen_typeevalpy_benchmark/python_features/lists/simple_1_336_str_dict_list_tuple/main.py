# Functions are assigned as elements of a list and then called.


def func1():
    return 'bidke'


def func2():
    return {'vxidu': 65, 'nabpk': 39, 'ajkav': 83}


def func3():
    return [83, 76, 95]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (43, 85, 12)


b = ["Hello"]
b[0] = func4

f = b[0]()
