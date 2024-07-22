# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 'wtytj'


def func3():
    return {'dpnyg': 58, 'binwi': 85, 'khpkc': 19}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 33.54


b = ["Hello"]
b[0] = func4

f = b[0]()
