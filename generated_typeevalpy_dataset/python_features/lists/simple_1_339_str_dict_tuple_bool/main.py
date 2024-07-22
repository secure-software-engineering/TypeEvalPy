# Functions are assigned as elements of a list and then called.


def func1():
    return 'afppb'


def func2():
    return {'kvuoe': 95, 'bykyt': 8, 'sfttn': 41}


def func3():
    return (1, 14, 72)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
