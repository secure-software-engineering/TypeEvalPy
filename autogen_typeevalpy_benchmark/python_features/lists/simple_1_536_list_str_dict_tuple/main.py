# Functions are assigned as elements of a list and then called.


def func1():
    return [21, 7, 26]


def func2():
    return 'awuzc'


def func3():
    return {'zylel': 99, 'tkmrh': 70, 'hyerx': 73}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (29, 46, 75)


b = ["Hello"]
b[0] = func4

f = b[0]()
