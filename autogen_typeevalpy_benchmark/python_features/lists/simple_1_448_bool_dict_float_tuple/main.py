# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'uvcui': 24, 'yvhhk': 56, 'dacju': 79}


def func3():
    return 42.12


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (54, 62, 21)


b = ["Hello"]
b[0] = func4

f = b[0]()
