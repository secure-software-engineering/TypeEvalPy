# Functions are assigned as elements of a list and then called.


def func1():
    return 47


def func2():
    return 60.79


def func3():
    return (73, 2, 49)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'opztc': 79, 'augtl': 69, 'lwhgt': 46}


b = ["Hello"]
b[0] = func4

f = b[0]()
