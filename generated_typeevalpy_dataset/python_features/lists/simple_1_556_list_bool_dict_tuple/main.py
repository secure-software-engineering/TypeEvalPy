# Functions are assigned as elements of a list and then called.


def func1():
    return [85, 19, 60]


def func2():
    return True


def func3():
    return {'dnzhe': 64, 'pbnyw': 71, 'xhcjn': 55}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (3, 15, 11)


b = ["Hello"]
b[0] = func4

f = b[0]()
