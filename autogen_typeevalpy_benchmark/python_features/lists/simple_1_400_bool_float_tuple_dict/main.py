# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return 40.12


def func3():
    return (41, 79, 26)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'prtxn': 33, 'hxdfx': 41, 'pnwfe': 6}


b = ["Hello"]
b[0] = func4

f = b[0]()
