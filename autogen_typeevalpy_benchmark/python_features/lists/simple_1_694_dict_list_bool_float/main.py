# Functions are assigned as elements of a list and then called.


def func1():
    return {'ytscd': 57, 'oxptz': 57, 'ynbgx': 60}


def func2():
    return [16, 50, 26]


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 69.1


b = ["Hello"]
b[0] = func4

f = b[0]()
