# Functions are assigned as elements of a list and then called.


def func1():
    return 23


def func2():
    return (12, 9, 57)


def func3():
    return {'thupe': 90, 'rgaap': 96, 'xggbg': 48}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'nfkju'


b = ["Hello"]
b[0] = func4

f = b[0]()
