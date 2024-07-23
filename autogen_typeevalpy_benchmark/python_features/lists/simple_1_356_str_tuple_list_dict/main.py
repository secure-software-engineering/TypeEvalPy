# Functions are assigned as elements of a list and then called.


def func1():
    return 'syqvw'


def func2():
    return (1, 65, 37)


def func3():
    return [70, 57, 91]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ulsug': 45, 'vhfsu': 11, 'togkb': 52}


b = ["Hello"]
b[0] = func4

f = b[0]()
