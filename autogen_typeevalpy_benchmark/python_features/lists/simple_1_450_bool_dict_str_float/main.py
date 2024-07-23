# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'ucdft': 31, 'hmqvf': 36, 'ikfyv': 74}


def func3():
    return 'olpcw'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 30.72


b = ["Hello"]
b[0] = func4

f = b[0]()
