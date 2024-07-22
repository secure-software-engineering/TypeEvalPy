# Functions are assigned as elements of a list and then called.


def func1():
    return {'mcyzo': 95, 'ykixs': 27, 'ducxn': 5}


def func2():
    return (21, 75, 71)


def func3():
    return 43.82


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
