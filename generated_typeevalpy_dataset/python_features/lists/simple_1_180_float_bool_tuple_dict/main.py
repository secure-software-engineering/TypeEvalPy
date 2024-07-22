# Functions are assigned as elements of a list and then called.


def func1():
    return 51.84


def func2():
    return False


def func3():
    return (59, 23, 40)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'wimpu': 90, 'doypi': 25, 'vrfrn': 13}


b = ["Hello"]
b[0] = func4

f = b[0]()
