# Functions are assigned as elements of a list and then called.


def func1():
    return [13, 2, 3]


def func2():
    return {'hniqv': 11, 'intye': 69, 'jtkbp': 30}


def func3():
    return 48.65


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (46, 27, 80)


b = ["Hello"]
b[0] = func4

f = b[0]()
