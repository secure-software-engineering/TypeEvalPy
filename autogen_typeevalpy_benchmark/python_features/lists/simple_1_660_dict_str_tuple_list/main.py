# Functions are assigned as elements of a list and then called.


def func1():
    return {'rbjgp': 96, 'aegiu': 33, 'ltvcv': 90}


def func2():
    return 'gpiaz'


def func3():
    return (38, 97, 91)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [86, 82, 86]


b = ["Hello"]
b[0] = func4

f = b[0]()
