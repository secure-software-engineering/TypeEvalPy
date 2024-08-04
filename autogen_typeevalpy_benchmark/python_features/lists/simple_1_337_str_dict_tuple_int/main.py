# Functions are assigned as elements of a list and then called.


def func1():
    return 'mxxdb'


def func2():
    return {'hfanl': 25, 'olyke': 42, 'wngdf': 71}


def func3():
    return (84, 7, 23)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 88


b = ["Hello"]
b[0] = func4

f = b[0]()
