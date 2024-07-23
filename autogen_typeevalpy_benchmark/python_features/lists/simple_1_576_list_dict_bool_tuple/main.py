# Functions are assigned as elements of a list and then called.


def func1():
    return [85, 84, 16]


def func2():
    return {'gmeec': 100, 'kpbvs': 19, 'ayhzi': 47}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (9, 79, 29)


b = ["Hello"]
b[0] = func4

f = b[0]()
