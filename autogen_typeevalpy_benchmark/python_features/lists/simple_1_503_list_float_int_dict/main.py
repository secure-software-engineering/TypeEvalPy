# Functions are assigned as elements of a list and then called.


def func1():
    return [77, 32, 6]


def func2():
    return 28.94


def func3():
    return 68


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'klgoo': 80, 'gyash': 39, 'dbstc': 15}


b = ["Hello"]
b[0] = func4

f = b[0]()
