# Functions are assigned as elements of a list and then called.


def func1():
    return {'ecyvg': 8, 'muutb': 25, 'rxnua': 57}


def func2():
    return (1, 70, 54)


def func3():
    return 9


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
