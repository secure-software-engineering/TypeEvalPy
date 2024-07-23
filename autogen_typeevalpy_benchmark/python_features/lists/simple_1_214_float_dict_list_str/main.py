# Functions are assigned as elements of a list and then called.


def func1():
    return 17.62


def func2():
    return {'wpmsk': 19, 'xvspx': 76, 'uafzu': 64}


def func3():
    return [72, 61, 12]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'dixbn'


b = ["Hello"]
b[0] = func4

f = b[0]()
