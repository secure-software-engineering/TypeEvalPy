# Functions are assigned as elements of a list and then called.


def func1():
    return 68.72


def func2():
    return 'touqt'


def func3():
    return (5, 53, 30)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'cqthl': 18, 'shenx': 31, 'ioeyn': 13}


b = ["Hello"]
b[0] = func4

f = b[0]()
