# Functions are assigned as elements of a list and then called.


def func1():
    return 'uvwsy'


def func2():
    return [6, 92, 30]


def func3():
    return {'vnvhn': 80, 'rrkhn': 65, 'cgbbs': 60}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (60, 95, 86)


b = ["Hello"]
b[0] = func4

f = b[0]()
