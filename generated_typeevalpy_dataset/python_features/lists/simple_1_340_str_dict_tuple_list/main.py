# Functions are assigned as elements of a list and then called.


def func1():
    return 'qbrcb'


def func2():
    return {'akyzw': 49, 'pfdzq': 94, 'aevwg': 79}


def func3():
    return (60, 33, 74)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [95, 97, 71]


b = ["Hello"]
b[0] = func4

f = b[0]()
