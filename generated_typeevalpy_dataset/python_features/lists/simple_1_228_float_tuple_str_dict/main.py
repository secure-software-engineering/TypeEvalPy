# Functions are assigned as elements of a list and then called.


def func1():
    return 30.83


def func2():
    return (14, 94, 47)


def func3():
    return 'heqkw'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'mtyqb': 12, 'qhmsy': 15, 'pvlov': 31}


b = ["Hello"]
b[0] = func4

f = b[0]()
