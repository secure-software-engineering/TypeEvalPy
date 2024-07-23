# Functions are assigned as elements of a list and then called.


def func1():
    return {'ebxrg': 75, 'vniuw': 23, 'uwojt': 65}


def func2():
    return 3


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (76, 75, 60)


b = ["Hello"]
b[0] = func4

f = b[0]()
