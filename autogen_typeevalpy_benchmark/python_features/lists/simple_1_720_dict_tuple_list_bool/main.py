# Functions are assigned as elements of a list and then called.


def func1():
    return {'ixbjb': 89, 'pobql': 9, 'iauqc': 42}


def func2():
    return (3, 86, 90)


def func3():
    return [39, 14, 22]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
