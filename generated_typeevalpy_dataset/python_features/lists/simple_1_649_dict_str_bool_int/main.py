# Functions are assigned as elements of a list and then called.


def func1():
    return {'qhota': 47, 'ibpqb': 94, 'lidhr': 12}


def func2():
    return 'cqexf'


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 68


b = ["Hello"]
b[0] = func4

f = b[0]()
