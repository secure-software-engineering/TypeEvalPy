# Functions are assigned as elements of a list and then called.


def func1():
    return {'hhabb': 92, 'tuvom': 91, 'uozml': 93}


def func2():
    return 64.66


def func3():
    return [53, 45, 16]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'zwpgt'


b = ["Hello"]
b[0] = func4

f = b[0]()
