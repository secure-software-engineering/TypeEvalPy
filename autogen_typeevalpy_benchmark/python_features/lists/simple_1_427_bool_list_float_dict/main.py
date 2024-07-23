# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return [55, 49, 37]


def func3():
    return 84.31


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'cmbua': 94, 'uccka': 86, 'qnehw': 60}


b = ["Hello"]
b[0] = func4

f = b[0]()
