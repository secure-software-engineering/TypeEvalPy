# Functions are assigned as elements of a list and then called.


def func1():
    return 7


def func2():
    return [70, 17, 8]


def func3():
    return (43, 51, 27)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'attzz': 12, 'ylalp': 90, 'ikchq': 23}


b = ["Hello"]
b[0] = func4

f = b[0]()
