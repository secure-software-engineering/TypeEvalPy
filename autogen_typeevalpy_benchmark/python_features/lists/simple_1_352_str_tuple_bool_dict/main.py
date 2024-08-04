# Functions are assigned as elements of a list and then called.


def func1():
    return 'tmuvw'


def func2():
    return (25, 95, 95)


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'afqoj': 34, 'oxvrn': 81, 'hfrxf': 2}


b = ["Hello"]
b[0] = func4

f = b[0]()
