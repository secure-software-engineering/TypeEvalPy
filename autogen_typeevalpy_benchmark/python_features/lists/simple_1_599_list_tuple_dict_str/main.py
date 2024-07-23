# Functions are assigned as elements of a list and then called.


def func1():
    return [34, 95, 13]


def func2():
    return (13, 25, 2)


def func3():
    return {'lsgqw': 23, 'zjoft': 17, 'ewspc': 15}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'dglbi'


b = ["Hello"]
b[0] = func4

f = b[0]()
