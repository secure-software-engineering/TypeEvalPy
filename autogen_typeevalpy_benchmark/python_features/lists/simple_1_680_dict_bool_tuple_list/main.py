# Functions are assigned as elements of a list and then called.


def func1():
    return {'dbqlj': 42, 'eptur': 98, 'ldgku': 30}


def func2():
    return True


def func3():
    return (87, 7, 61)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [51, 82, 75]


b = ["Hello"]
b[0] = func4

f = b[0]()
