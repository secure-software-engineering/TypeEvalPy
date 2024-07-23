# Functions are assigned as elements of a list and then called.


def func1():
    return 43.4


def func2():
    return [18, 78, 67]


def func3():
    return {'pkfre': 76, 'pywwu': 85, 'vrbrr': 22}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 96


b = ["Hello"]
b[0] = func4

f = b[0]()
