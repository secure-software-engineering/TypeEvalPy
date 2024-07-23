# Functions are assigned as elements of a list and then called.


def func1():
    return 'ixuvz'


def func2():
    return [1, 38, 41]


def func3():
    return {'ivppl': 21, 'maqmz': 20, 'lizqw': 65}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 22.1


b = ["Hello"]
b[0] = func4

f = b[0]()
