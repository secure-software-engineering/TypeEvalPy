# Functions are assigned as elements of a list and then called.


def func1():
    return (80, 28, 75)


def func2():
    return [69, 29, 5]


def func3():
    return 'leams'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'mgpje': 45, 'murze': 69, 'yodct': 17}


b = ["Hello"]
b[0] = func4

f = b[0]()
