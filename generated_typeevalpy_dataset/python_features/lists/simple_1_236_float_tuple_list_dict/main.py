# Functions are assigned as elements of a list and then called.


def func1():
    return 64.55


def func2():
    return (30, 67, 69)


def func3():
    return [54, 29, 65]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'gsbkk': 53, 'nlwzf': 28, 'kdicy': 4}


b = ["Hello"]
b[0] = func4

f = b[0]()
