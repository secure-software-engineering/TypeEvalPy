# Functions are assigned as elements of a list and then called.


def func1():
    return [26, 31, 7]


def func2():
    return {'oenkp': 79, 'qeafi': 36, 'cpsfx': 83}


def func3():
    return 11.46


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (97, 46, 84)


b = ["Hello"]
b[0] = func4

f = b[0]()
