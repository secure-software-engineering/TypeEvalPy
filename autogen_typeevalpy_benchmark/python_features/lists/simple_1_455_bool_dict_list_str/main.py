# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'eqtqy': 35, 'ynlqz': 50, 'ytoef': 27}


def func3():
    return [100, 38, 14]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'erkfv'


b = ["Hello"]
b[0] = func4

f = b[0]()
