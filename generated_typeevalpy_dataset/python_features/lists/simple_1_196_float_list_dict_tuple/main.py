# Functions are assigned as elements of a list and then called.


def func1():
    return 67.58


def func2():
    return [47, 26, 70]


def func3():
    return {'nflyt': 33, 'aoftu': 49, 'zkprj': 62}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (77, 21, 94)


b = ["Hello"]
b[0] = func4

f = b[0]()
