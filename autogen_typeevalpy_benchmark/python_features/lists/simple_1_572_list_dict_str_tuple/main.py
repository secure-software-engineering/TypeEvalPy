# Functions are assigned as elements of a list and then called.


def func1():
    return [35, 91, 71]


def func2():
    return {'rhnnl': 79, 'qpqdg': 27, 'zvbla': 40}


def func3():
    return 'qcgzm'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (89, 8, 78)


b = ["Hello"]
b[0] = func4

f = b[0]()
