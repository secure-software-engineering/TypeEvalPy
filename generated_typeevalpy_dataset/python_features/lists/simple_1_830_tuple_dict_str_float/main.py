# Functions are assigned as elements of a list and then called.


def func1():
    return (33, 38, 21)


def func2():
    return {'klpfn': 24, 'csksu': 94, 'dhghs': 30}


def func3():
    return 'gaihu'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 61.86


b = ["Hello"]
b[0] = func4

f = b[0]()
