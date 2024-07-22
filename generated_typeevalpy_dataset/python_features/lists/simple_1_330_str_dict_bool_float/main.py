# Functions are assigned as elements of a list and then called.


def func1():
    return 'xqkox'


def func2():
    return {'yitgw': 61, 'cmggj': 84, 'rosdx': 33}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 40.21


b = ["Hello"]
b[0] = func4

f = b[0]()
