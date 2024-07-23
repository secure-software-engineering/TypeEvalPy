# Functions are assigned as elements of a list and then called.


def func1():
    return {'zinyz': 7, 'nkgah': 71, 'yhiqt': 76}


def func2():
    return 73


def func3():
    return [50, 90, 89]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'bvmea'


b = ["Hello"]
b[0] = func4

f = b[0]()
