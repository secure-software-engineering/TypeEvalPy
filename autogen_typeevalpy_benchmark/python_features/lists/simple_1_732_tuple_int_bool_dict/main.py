# Functions are assigned as elements of a list and then called.


def func1():
    return (15, 55, 78)


def func2():
    return 1


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'vigmi': 52, 'thngy': 23, 'gphte': 54}


b = ["Hello"]
b[0] = func4

f = b[0]()
