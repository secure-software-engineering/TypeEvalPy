# Functions are assigned as elements of a list and then called.


def func1():
    return (51, 70, 84)


def func2():
    return 60.47


def func3():
    return {'cygdr': 36, 'glacl': 24, 'colqi': 91}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [83, 31, 6]


b = ["Hello"]
b[0] = func4

f = b[0]()
