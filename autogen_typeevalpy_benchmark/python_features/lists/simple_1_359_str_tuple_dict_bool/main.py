# Functions are assigned as elements of a list and then called.


def func1():
    return 'vtplz'


def func2():
    return (90, 42, 10)


def func3():
    return {'jdzlg': 53, 'bevzt': 38, 'dcqnk': 77}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
