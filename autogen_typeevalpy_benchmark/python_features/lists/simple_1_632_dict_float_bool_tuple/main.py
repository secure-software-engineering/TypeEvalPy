# Functions are assigned as elements of a list and then called.


def func1():
    return {'rgkfb': 3, 'eajbl': 74, 'vshrk': 90}


def func2():
    return 94.22


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (46, 67, 18)


b = ["Hello"]
b[0] = func4

f = b[0]()
