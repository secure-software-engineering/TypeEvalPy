# Functions are assigned as elements of a list and then called.


def func1():
    return [6, 98, 79]


def func2():
    return (56, 100, 85)


def func3():
    return {'xhmyx': 68, 'lilpu': 80, 'blpzr': 75}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
