# Functions are assigned as elements of a list and then called.


def func1():
    return {'bybez': 78, 'ewyod': 96, 'chrol': 59}


def func2():
    return 32.76


def func3():
    return [74, 21, 85]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
