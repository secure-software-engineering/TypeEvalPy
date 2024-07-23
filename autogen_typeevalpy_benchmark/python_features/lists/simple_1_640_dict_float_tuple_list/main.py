# Functions are assigned as elements of a list and then called.


def func1():
    return {'amhsq': 22, 'egegq': 91, 'jakyz': 46}


def func2():
    return 37.97


def func3():
    return (85, 21, 41)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [12, 67, 30]


b = ["Hello"]
b[0] = func4

f = b[0]()
