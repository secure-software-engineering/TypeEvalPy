# Functions are assigned as elements of a list and then called.


def func1():
    return (29, 25, 23)


def func2():
    return [95, 98, 50]


def func3():
    return {'ggjnk': 47, 'phxuw': 53, 'qkczp': 60}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'htqrp'


b = ["Hello"]
b[0] = func4

f = b[0]()
