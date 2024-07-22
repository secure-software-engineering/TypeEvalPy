# Functions are assigned as elements of a list and then called.


def func1():
    return (77, 67, 80)


def func2():
    return 'grhgs'


def func3():
    return {'ibtcn': 33, 'otxmn': 57, 'ythyh': 7}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 88.83


b = ["Hello"]
b[0] = func4

f = b[0]()
