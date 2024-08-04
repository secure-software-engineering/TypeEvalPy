# Functions are assigned as elements of a list and then called.


def func1():
    return (61, 26, 62)


def func2():
    return [5, 35, 22]


def func3():
    return 'ubhjg'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'lytmb': 27, 'aoixb': 66, 'qfimg': 84}


b = ["Hello"]
b[0] = func4

f = b[0]()
