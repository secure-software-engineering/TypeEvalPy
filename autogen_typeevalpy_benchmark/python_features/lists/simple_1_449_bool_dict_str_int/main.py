# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return {'raxnn': 18, 'yxdxf': 56, 'cvtcs': 14}


def func3():
    return 'ookpg'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 100


b = ["Hello"]
b[0] = func4

f = b[0]()
