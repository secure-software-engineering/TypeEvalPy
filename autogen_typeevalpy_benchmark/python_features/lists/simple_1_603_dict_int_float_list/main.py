# Functions are assigned as elements of a list and then called.


def func1():
    return {'wljre': 18, 'hsbyc': 50, 'wvcko': 48}


def func2():
    return 70


def func3():
    return 69.87


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [42, 82, 23]


b = ["Hello"]
b[0] = func4

f = b[0]()
