# Functions are assigned as elements of a list and then called.


def func1():
    return 'omvlz'


def func2():
    return 73.17


def func3():
    return (5, 24, 88)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'eolyl': 33, 'zxgxy': 19, 'cqpjd': 63}


b = ["Hello"]
b[0] = func4

f = b[0]()
