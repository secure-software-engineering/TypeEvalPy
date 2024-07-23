# Functions are assigned as elements of a list and then called.


def func1():
    return {'arvej': 55, 'memtl': 24, 'psepa': 47}


def func2():
    return 'elgkw'


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 79


b = ["Hello"]
b[0] = func4

f = b[0]()
