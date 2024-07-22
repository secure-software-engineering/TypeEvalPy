# Functions are assigned as elements of a list and then called.


def func1():
    return 75.85


def func2():
    return {'scyby': 71, 'zzgkk': 74, 'crqxx': 20}


def func3():
    return (83, 75, 24)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 5


b = ["Hello"]
b[0] = func4

f = b[0]()
