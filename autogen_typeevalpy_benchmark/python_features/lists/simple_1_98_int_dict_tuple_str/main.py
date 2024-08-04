# Functions are assigned as elements of a list and then called.


def func1():
    return 46


def func2():
    return {'lxhol': 65, 'vlrix': 3, 'mlfru': 6}


def func3():
    return (60, 41, 5)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'tkdrg'


b = ["Hello"]
b[0] = func4

f = b[0]()
