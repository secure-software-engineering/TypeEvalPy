# Functions are assigned as elements of a list and then called.


def func1():
    return {'lcmpe': 18, 'ocvfy': 54, 'jehfp': 77}


def func2():
    return 'lnfdz'


def func3():
    return (23, 99, 7)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
