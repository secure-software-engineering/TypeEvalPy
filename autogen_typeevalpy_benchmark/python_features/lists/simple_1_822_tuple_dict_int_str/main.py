# Functions are assigned as elements of a list and then called.


def func1():
    return (40, 89, 72)


def func2():
    return {'kakkd': 81, 'ldkpb': 4, 'vbuwn': 23}


def func3():
    return 49


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'xuvhx'


b = ["Hello"]
b[0] = func4

f = b[0]()
