# Functions are assigned as elements of a list and then called.


def func1():
    return [55, 69, 36]


def func2():
    return 42


def func3():
    return {'iiqre': 52, 'amgnn': 100, 'bqosn': 93}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
