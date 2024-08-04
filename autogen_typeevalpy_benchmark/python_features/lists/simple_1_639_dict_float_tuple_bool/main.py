# Functions are assigned as elements of a list and then called.


def func1():
    return {'fexbs': 18, 'uwqim': 3, 'rhdav': 96}


def func2():
    return 70.0


def func3():
    return (12, 67, 54)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
