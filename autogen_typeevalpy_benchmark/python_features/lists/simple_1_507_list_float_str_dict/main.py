# Functions are assigned as elements of a list and then called.


def func1():
    return [27, 93, 74]


def func2():
    return 44.15


def func3():
    return 'ddvze'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'crqcu': 2, 'avxlp': 54, 'rdlys': 89}


b = ["Hello"]
b[0] = func4

f = b[0]()
