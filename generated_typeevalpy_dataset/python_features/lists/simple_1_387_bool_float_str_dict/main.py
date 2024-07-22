# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 77.08


def func3():
    return 'ivbbc'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'icowz': 87, 'myzqw': 33, 'jenqn': 72}


b = ["Hello"]
b[0] = func4

f = b[0]()
