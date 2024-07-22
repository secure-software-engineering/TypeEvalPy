# Functions are assigned as elements of a list and then called.


def func1():
    return {'nuosy': 44, 'llfyn': 73, 'rupgr': 11}


def func2():
    return 77.97


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (88, 63, 82)


b = ["Hello"]
b[0] = func4

f = b[0]()
