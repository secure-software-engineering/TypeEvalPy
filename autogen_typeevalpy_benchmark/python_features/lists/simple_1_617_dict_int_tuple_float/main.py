# Functions are assigned as elements of a list and then called.


def func1():
    return {'cltgo': 86, 'zwmpy': 91, 'fafus': 50}


def func2():
    return 73


def func3():
    return (59, 18, 66)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 56.5


b = ["Hello"]
b[0] = func4

f = b[0]()
