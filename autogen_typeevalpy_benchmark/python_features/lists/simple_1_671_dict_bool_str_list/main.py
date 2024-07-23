# Functions are assigned as elements of a list and then called.


def func1():
    return {'wifkk': 12, 'qtxjl': 79, 'utqoc': 96}


def func2():
    return False


def func3():
    return 'onzot'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [46, 17, 71]


b = ["Hello"]
b[0] = func4

f = b[0]()
