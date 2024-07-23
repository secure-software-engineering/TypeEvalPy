# Functions are assigned as elements of a list and then called.


def func1():
    return 'hkenf'


def func2():
    return {'nfqec': 41, 'ssgeq': 89, 'fbfem': 13}


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (12, 59, 2)


b = ["Hello"]
b[0] = func4

f = b[0]()
