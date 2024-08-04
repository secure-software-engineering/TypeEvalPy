# Functions are assigned as elements of a list and then called.


def func1():
    return [26, 74, 44]


def func2():
    return 52.54


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'haisq': 46, 'zpimw': 51, 'xmsxp': 71}


b = ["Hello"]
b[0] = func4

f = b[0]()
