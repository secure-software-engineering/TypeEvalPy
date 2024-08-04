# Functions are assigned as elements of a list and then called.


def func1():
    return 'ecrqe'


def func2():
    return [93, 6, 5]


def func3():
    return 73.66


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'adrhz': 7, 'zeroq': 17, 'ojtfv': 13}


b = ["Hello"]
b[0] = func4

f = b[0]()
