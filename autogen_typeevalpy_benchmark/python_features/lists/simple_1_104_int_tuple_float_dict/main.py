# Functions are assigned as elements of a list and then called.


def func1():
    return 37


def func2():
    return (29, 99, 40)


def func3():
    return 30.07


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'cviwa': 75, 'oxokd': 49, 'stepq': 31}


b = ["Hello"]
b[0] = func4

f = b[0]()
