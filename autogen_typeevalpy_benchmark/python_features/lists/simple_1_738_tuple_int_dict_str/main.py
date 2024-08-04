# Functions are assigned as elements of a list and then called.


def func1():
    return (99, 35, 53)


def func2():
    return 91


def func3():
    return {'jkixa': 26, 'nauej': 59, 'jentp': 82}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'oargc'


b = ["Hello"]
b[0] = func4

f = b[0]()
