# Functions are assigned as elements of a list and then called.


def func1():
    return 72.01


def func2():
    return 'xljko'


def func3():
    return {'dupdf': 92, 'mvhcy': 11, 'wxcyr': 76}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
