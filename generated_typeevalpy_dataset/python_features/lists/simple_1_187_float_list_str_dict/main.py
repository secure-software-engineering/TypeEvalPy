# Functions are assigned as elements of a list and then called.


def func1():
    return 27.59


def func2():
    return [88, 49, 23]


def func3():
    return 'ziupc'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'eyywx': 34, 'kgugl': 71, 'sinqf': 75}


b = ["Hello"]
b[0] = func4

f = b[0]()
