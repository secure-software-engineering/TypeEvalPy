# Functions are assigned as elements of a list and then called.


def func1():
    return {'gvajk': 58, 'fwcfo': 96, 'lazvg': 22}


def func2():
    return (46, 23, 86)


def func3():
    return 25.24


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [50, 96, 34]


b = ["Hello"]
b[0] = func4

f = b[0]()
