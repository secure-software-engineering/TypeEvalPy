# Functions are assigned as elements of a list and then called.


def func1():
    return {'zltrj': 64, 'isoxb': 49, 'rcvjo': 1}


def func2():
    return False


def func3():
    return 'wxhua'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 49


b = ["Hello"]
b[0] = func4

f = b[0]()
