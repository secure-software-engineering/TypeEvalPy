# Functions are assigned as elements of a list and then called.


def func1():
    return [77, 1, 25]


def func2():
    return (77, 23, 100)


def func3():
    return {'rfotr': 35, 'btjqy': 65, 'qxmuz': 12}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 11.99


b = ["Hello"]
b[0] = func4

f = b[0]()
