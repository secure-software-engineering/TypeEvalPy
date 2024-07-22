# Functions are assigned as elements of a list and then called.


def func1():
    return [35, 19, 89]


def func2():
    return 71.09


def func3():
    return {'tenrf': 40, 'mjppv': 45, 'ytihj': 12}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
