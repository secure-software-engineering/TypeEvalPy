# Functions are assigned as elements of a list and then called.


def func1():
    return {'xbrbz': 34, 'pmcyq': 1, 'gdxlz': 72}


def func2():
    return (79, 72, 68)


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 61


b = ["Hello"]
b[0] = func4

f = b[0]()
