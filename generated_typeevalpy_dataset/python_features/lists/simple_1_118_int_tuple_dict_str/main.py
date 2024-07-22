# Functions are assigned as elements of a list and then called.


def func1():
    return 68


def func2():
    return (39, 74, 46)


def func3():
    return {'evyme': 23, 'ldrvf': 2, 'tohzu': 18}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'bqgwm'


b = ["Hello"]
b[0] = func4

f = b[0]()
