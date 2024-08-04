# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return [58, 78, 73]


def func3():
    return {'phzvb': 72, 'iwkoe': 55, 'lkcax': 61}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 25


b = ["Hello"]
b[0] = func4

f = b[0]()
