# Functions are assigned as elements of a list and then called.


def func1():
    return (47, 65, 34)


def func2():
    return {'slmmz': 67, 'ayvhb': 45, 'xeunw': 20}


def func3():
    return 10.92


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'tchke'


b = ["Hello"]
b[0] = func4

f = b[0]()
