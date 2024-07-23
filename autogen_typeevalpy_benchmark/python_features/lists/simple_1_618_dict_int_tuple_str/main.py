# Functions are assigned as elements of a list and then called.


def func1():
    return {'ztvhy': 26, 'kimbg': 23, 'ulllg': 48}


def func2():
    return 56


def func3():
    return (50, 11, 64)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ljrya'


b = ["Hello"]
b[0] = func4

f = b[0]()
