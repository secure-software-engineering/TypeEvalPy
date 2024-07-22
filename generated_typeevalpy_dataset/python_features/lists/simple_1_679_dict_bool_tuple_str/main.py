# Functions are assigned as elements of a list and then called.


def func1():
    return {'vulpw': 89, 'uzcij': 52, 'cxkgg': 11}


def func2():
    return True


def func3():
    return (8, 16, 70)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ahgsl'


b = ["Hello"]
b[0] = func4

f = b[0]()
