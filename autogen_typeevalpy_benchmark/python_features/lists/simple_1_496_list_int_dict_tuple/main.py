# Functions are assigned as elements of a list and then called.


def func1():
    return [85, 93, 65]


def func2():
    return 14


def func3():
    return {'nthhj': 91, 'vqlmq': 48, 'tgrfy': 11}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (33, 31, 48)


b = ["Hello"]
b[0] = func4

f = b[0]()
