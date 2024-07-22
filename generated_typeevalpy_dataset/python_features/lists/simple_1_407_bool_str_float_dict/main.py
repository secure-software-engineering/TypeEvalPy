# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 'obler'


def func3():
    return 14.82


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'tjpzu': 87, 'ocfdp': 83, 'azuvh': 36}


b = ["Hello"]
b[0] = func4

f = b[0]()
