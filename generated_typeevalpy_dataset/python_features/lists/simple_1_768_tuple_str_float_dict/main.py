# Functions are assigned as elements of a list and then called.


def func1():
    return (40, 39, 36)


def func2():
    return 'mnkpe'


def func3():
    return 77.54


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'esips': 67, 'izori': 52, 'dbrbb': 57}


b = ["Hello"]
b[0] = func4

f = b[0]()
