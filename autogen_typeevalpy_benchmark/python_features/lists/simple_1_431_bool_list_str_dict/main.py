# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return [46, 100, 92]


def func3():
    return 'fvqmn'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'mmjsu': 23, 'msxeu': 69, 'egmir': 86}


b = ["Hello"]
b[0] = func4

f = b[0]()
