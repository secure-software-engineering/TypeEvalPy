# Functions are assigned as elements of a list and then called.


def func1():
    return (22, 77, 56)


def func2():
    return 'zjpjd'


def func3():
    return [90, 66, 30]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'dtfmg': 44, 'ovvpp': 35, 'kljcy': 99}


b = ["Hello"]
b[0] = func4

f = b[0]()
