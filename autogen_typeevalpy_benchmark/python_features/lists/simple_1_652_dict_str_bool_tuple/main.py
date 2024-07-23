# Functions are assigned as elements of a list and then called.


def func1():
    return {'lzitm': 9, 'tjfks': 88, 'dttvs': 84}


def func2():
    return 'hgnay'


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (66, 65, 31)


b = ["Hello"]
b[0] = func4

f = b[0]()
