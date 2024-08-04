# Functions are assigned as elements of a list and then called.


def func1():
    return 57


def func2():
    return {'selyx': 50, 'nfbpr': 85, 'vdyco': 61}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (63, 58, 86)


b = ["Hello"]
b[0] = func4

f = b[0]()
