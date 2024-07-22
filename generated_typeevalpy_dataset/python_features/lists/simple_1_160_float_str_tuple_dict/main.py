# Functions are assigned as elements of a list and then called.


def func1():
    return 43.93


def func2():
    return 'babmd'


def func3():
    return (34, 48, 33)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'utxpe': 73, 'ovnqp': 11, 'xxksg': 35}


b = ["Hello"]
b[0] = func4

f = b[0]()
