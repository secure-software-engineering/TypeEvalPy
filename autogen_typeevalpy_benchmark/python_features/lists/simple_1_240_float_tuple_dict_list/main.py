# Functions are assigned as elements of a list and then called.


def func1():
    return 9.37


def func2():
    return (94, 1, 45)


def func3():
    return {'jysdg': 100, 'oomtn': 33, 'kclas': 21}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [90, 99, 35]


b = ["Hello"]
b[0] = func4

f = b[0]()
