# Functions are assigned as elements of a list and then called.


def func1():
    return {'pqbwn': 20, 'lddbi': 49, 'atylm': 77}


def func2():
    return 55


def func3():
    return (100, 51, 57)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'fqxny'


b = ["Hello"]
b[0] = func4

f = b[0]()
