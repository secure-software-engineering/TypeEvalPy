# Functions are assigned as elements of a list and then called.


def func1():
    return 80


def func2():
    return 'gsjni'


def func3():
    return (73, 62, 26)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'lvvgx': 100, 'ziztb': 14, 'hpnbk': 34}


b = ["Hello"]
b[0] = func4

f = b[0]()
