# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 89


def func3():
    return 80.0


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'kwftf': 22, 'cckbb': 99, 'wpifa': 97}


b = ["Hello"]
b[0] = func4

f = b[0]()
