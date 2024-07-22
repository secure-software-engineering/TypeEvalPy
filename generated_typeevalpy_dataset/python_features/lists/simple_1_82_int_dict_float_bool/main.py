# Functions are assigned as elements of a list and then called.


def func1():
    return 42


def func2():
    return {'wyksz': 20, 'izcfo': 93, 'mjjjz': 33}


def func3():
    return 4.05


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
