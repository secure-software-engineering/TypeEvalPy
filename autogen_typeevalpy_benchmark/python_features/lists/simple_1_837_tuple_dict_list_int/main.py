# Functions are assigned as elements of a list and then called.


def func1():
    return (60, 69, 88)


def func2():
    return {'apewd': 35, 'nuron': 40, 'foplj': 4}


def func3():
    return [4, 78, 37]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 77


b = ["Hello"]
b[0] = func4

f = b[0]()
