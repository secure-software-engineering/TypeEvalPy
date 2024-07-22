# Functions are assigned as elements of a list and then called.


def func1():
    return 'qrgiu'


def func2():
    return (94, 13, 38)


def func3():
    return {'nlddw': 37, 'bokze': 58, 'sgeam': 40}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 75


b = ["Hello"]
b[0] = func4

f = b[0]()
