# Functions are assigned as elements of a list and then called.


def func1():
    return {'pezak': 9, 'jjkqq': 7, 'ubezl': 73}


def func2():
    return [48, 92, 47]


def func3():
    return (62, 100, 46)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
