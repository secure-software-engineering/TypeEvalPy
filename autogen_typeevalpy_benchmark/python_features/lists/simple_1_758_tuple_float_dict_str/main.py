# Functions are assigned as elements of a list and then called.


def func1():
    return (32, 9, 90)


def func2():
    return 97.84


def func3():
    return {'cpjxu': 11, 'wxeue': 99, 'lmeum': 83}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'byaqf'


b = ["Hello"]
b[0] = func4

f = b[0]()
