# Functions are assigned as elements of a list and then called.


def func1():
    return 30


def func2():
    return (36, 89, 51)


def func3():
    return 65.61


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'bczkn': 4, 'pftln': 67, 'gpdvd': 69}


b = ["Hello"]
b[0] = func4

f = b[0]()
