# Functions are assigned as elements of a list and then called.


def func1():
    return (2, 23, 52)


def func2():
    return [88, 74, 78]


def func3():
    return {'eufse': 2, 'rxbxl': 19, 'yzdii': 84}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 73


b = ["Hello"]
b[0] = func4

f = b[0]()
