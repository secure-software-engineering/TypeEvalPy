# Functions are assigned as elements of a list and then called.


def func1():
    return 9


def func2():
    return 44.45


def func3():
    return (90, 50, 55)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'znjvd': 40, 'suuov': 62, 'ngstb': 6}


b = ["Hello"]
b[0] = func4

f = b[0]()
