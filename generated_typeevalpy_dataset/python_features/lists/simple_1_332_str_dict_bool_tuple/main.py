# Functions are assigned as elements of a list and then called.


def func1():
    return 'mswwh'


def func2():
    return {'jnbno': 58, 'phxyi': 55, 'lyxzf': 55}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (37, 31, 41)


b = ["Hello"]
b[0] = func4

f = b[0]()
