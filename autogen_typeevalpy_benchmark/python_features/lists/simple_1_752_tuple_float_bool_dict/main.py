# Functions are assigned as elements of a list and then called.


def func1():
    return (22, 98, 81)


def func2():
    return 13.98


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'dznuz': 41, 'usbja': 53, 'wtjzo': 41}


b = ["Hello"]
b[0] = func4

f = b[0]()
