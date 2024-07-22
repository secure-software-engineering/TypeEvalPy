# Functions are assigned as elements of a list and then called.


def func1():
    return [79, 46, 52]


def func2():
    return {'kbmji': 77, 'xovoc': 65, 'kokat': 24}


def func3():
    return 86


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'qbnve'


b = ["Hello"]
b[0] = func4

f = b[0]()
