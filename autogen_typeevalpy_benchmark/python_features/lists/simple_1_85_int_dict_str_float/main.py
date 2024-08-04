# Functions are assigned as elements of a list and then called.


def func1():
    return 78


def func2():
    return {'tqqfh': 90, 'rcbkp': 45, 'rzxci': 82}


def func3():
    return 'jnqnj'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 77.46


b = ["Hello"]
b[0] = func4

f = b[0]()
