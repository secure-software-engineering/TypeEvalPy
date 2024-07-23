# Functions are assigned as elements of a list and then called.


def func1():
    return 'agpyf'


def func2():
    return 40.57


def func3():
    return {'fvfzy': 89, 'ihukd': 36, 'zamjl': 21}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [8, 22, 20]


b = ["Hello"]
b[0] = func4

f = b[0]()
