# Functions are assigned as elements of a list and then called.


def func1():
    return 80.64


def func2():
    return 'ilkme'


def func3():
    return {'gwoul': 91, 'ruckg': 34, 'wpzbv': 4}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (89, 76, 3)


b = ["Hello"]
b[0] = func4

f = b[0]()
