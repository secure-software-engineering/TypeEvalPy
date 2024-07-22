# Functions are assigned as elements of a list and then called.


def func1():
    return [14, 71, 29]


def func2():
    return 47


def func3():
    return 'txeuo'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'sdrex': 20, 'khyvo': 92, 'lsach': 45}


b = ["Hello"]
b[0] = func4

f = b[0]()
