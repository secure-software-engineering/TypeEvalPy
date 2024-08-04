# Functions are assigned as elements of a list and then called.


def func1():
    return 'oketq'


def func2():
    return 39


def func3():
    return [2, 78, 89]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (75, 5, 59)


b = ["Hello"]
b[0] = func4

f = b[0]()
