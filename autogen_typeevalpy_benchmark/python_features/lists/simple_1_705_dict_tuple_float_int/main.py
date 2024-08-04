# Functions are assigned as elements of a list and then called.


def func1():
    return {'wxszz': 92, 'dkegd': 66, 'zzgdc': 64}


def func2():
    return (56, 30, 4)


def func3():
    return 15.58


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 76


b = ["Hello"]
b[0] = func4

f = b[0]()
