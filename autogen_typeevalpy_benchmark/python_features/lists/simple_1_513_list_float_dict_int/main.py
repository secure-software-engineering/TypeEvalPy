# Functions are assigned as elements of a list and then called.


def func1():
    return [20, 17, 1]


def func2():
    return 64.68


def func3():
    return {'ekogp': 11, 'jiqbw': 10, 'puexh': 45}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 2


b = ["Hello"]
b[0] = func4

f = b[0]()
