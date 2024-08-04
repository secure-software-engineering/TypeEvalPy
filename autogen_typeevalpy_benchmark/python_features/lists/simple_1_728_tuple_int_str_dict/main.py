# Functions are assigned as elements of a list and then called.


def func1():
    return (83, 49, 35)


def func2():
    return 5


def func3():
    return 'zyrni'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ocjlc': 91, 'zllmz': 50, 'ldxbw': 14}


b = ["Hello"]
b[0] = func4

f = b[0]()
