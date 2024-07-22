# Functions are assigned as elements of a list and then called.


def func1():
    return {'zgiuu': 68, 'ioyqx': 6, 'eddwr': 52}


def func2():
    return False


def func3():
    return 'tnjmf'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 17


b = ["Hello"]
b[0] = func4

f = b[0]()
