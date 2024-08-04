# Functions are assigned as elements of a list and then called.


def func1():
    return (40, 61, 7)


def func2():
    return {'zmpva': 54, 'uarav': 39, 'rtqxt': 83}


def func3():
    return 57


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 1.69


b = ["Hello"]
b[0] = func4

f = b[0]()
