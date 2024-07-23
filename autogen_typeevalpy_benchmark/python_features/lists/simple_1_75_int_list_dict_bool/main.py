# Functions are assigned as elements of a list and then called.


def func1():
    return 66


def func2():
    return [73, 55, 13]


def func3():
    return {'zdawl': 17, 'pwhmh': 74, 'irihs': 36}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
