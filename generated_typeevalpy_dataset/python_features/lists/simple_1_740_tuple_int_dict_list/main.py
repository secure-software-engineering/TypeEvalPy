# Functions are assigned as elements of a list and then called.


def func1():
    return (57, 51, 49)


def func2():
    return 61


def func3():
    return {'yqzpr': 33, 'iitrc': 56, 'wqcdv': 35}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [5, 25, 25]


b = ["Hello"]
b[0] = func4

f = b[0]()
