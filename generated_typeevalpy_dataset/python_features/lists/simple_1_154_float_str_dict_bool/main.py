# Functions are assigned as elements of a list and then called.


def func1():
    return 86.59


def func2():
    return 'qklll'


def func3():
    return {'ewhyw': 43, 'nlsuw': 93, 'fehqi': 70}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
