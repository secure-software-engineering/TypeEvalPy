# Functions are assigned as elements of a list and then called.


def func1():
    return 'vxfab'


def func2():
    return [12, 13, 52]


def func3():
    return {'qgcod': 87, 'tmycs': 60, 'mbcfo': 35}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (3, 45, 97)


b = ["Hello"]
b[0] = func4

f = b[0]()
