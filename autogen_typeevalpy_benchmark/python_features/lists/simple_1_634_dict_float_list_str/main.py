# Functions are assigned as elements of a list and then called.


def func1():
    return {'bxjvp': 92, 'kcshl': 45, 'jrybs': 61}


def func2():
    return 13.17


def func3():
    return [62, 6, 50]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'dgaer'


b = ["Hello"]
b[0] = func4

f = b[0]()
