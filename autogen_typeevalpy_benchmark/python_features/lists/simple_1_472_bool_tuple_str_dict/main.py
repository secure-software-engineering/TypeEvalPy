# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return (79, 55, 37)


def func3():
    return 'ellaw'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'njjvt': 69, 'qbxii': 87, 'bdsqg': 83}


b = ["Hello"]
b[0] = func4

f = b[0]()
