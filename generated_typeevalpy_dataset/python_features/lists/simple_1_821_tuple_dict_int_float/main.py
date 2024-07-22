# Functions are assigned as elements of a list and then called.


def func1():
    return (55, 66, 62)


def func2():
    return {'dagey': 52, 'oracc': 89, 'mwogj': 23}


def func3():
    return 34


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 87.83


b = ["Hello"]
b[0] = func4

f = b[0]()
