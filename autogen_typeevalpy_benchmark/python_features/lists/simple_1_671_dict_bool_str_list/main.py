# Functions are assigned as elements of a list and then called.


def func1():
    return {'ertyr': 16, 'kskyl': 54, 'ljuzm': 33}


def func2():
    return True


def func3():
    return 'xecst'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [17, 26, 33]


b = ["Hello"]
b[0] = func4

f = b[0]()
