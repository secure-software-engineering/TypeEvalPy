# Functions are assigned as elements of a list and then called.


def func1():
    return 'toyee'


def func2():
    return {'hwusu': 37, 'znjqe': 26, 'zvyhs': 99}


def func3():
    return (94, 69, 24)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 92


b = ["Hello"]
b[0] = func4

f = b[0]()
