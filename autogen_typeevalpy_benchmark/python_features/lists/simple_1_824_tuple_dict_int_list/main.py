# Functions are assigned as elements of a list and then called.


def func1():
    return (58, 18, 79)


def func2():
    return {'ccddz': 22, 'pzjns': 49, 'hpfkq': 81}


def func3():
    return 99


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [90, 27, 12]


b = ["Hello"]
b[0] = func4

f = b[0]()
