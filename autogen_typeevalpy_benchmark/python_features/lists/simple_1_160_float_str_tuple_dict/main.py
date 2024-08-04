# Functions are assigned as elements of a list and then called.


def func1():
    return 83.94


def func2():
    return 'tmpax'


def func3():
    return (45, 72, 9)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'cdjbm': 16, 'olirq': 98, 'tbcdd': 100}


b = ["Hello"]
b[0] = func4

f = b[0]()
