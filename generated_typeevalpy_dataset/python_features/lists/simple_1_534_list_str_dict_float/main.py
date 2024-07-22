# Functions are assigned as elements of a list and then called.


def func1():
    return [81, 35, 62]


def func2():
    return 'faxjm'


def func3():
    return {'ijbmn': 56, 'dzpgw': 11, 'gaegx': 97}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 89.4


b = ["Hello"]
b[0] = func4

f = b[0]()
