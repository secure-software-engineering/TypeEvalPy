# Functions are assigned as elements of a list and then called.


def func1():
    return {'cqphv': 3, 'nxqcb': 3, 'yrktn': 41}


def func2():
    return 69


def func3():
    return (35, 34, 76)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 38.58


b = ["Hello"]
b[0] = func4

f = b[0]()
