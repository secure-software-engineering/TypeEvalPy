# Functions are assigned as elements of a list and then called.


def func1():
    return (63, 44, 99)


def func2():
    return False


def func3():
    return [10, 60, 79]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'aktic': 11, 'cqzhg': 19, 'mntru': 70}


b = ["Hello"]
b[0] = func4

f = b[0]()
