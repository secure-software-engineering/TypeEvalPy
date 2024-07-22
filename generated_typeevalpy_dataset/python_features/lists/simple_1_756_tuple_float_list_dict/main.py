# Functions are assigned as elements of a list and then called.


def func1():
    return (96, 56, 11)


def func2():
    return 33.89


def func3():
    return [47, 17, 79]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ozmtw': 6, 'yjqgz': 67, 'ujpjq': 74}


b = ["Hello"]
b[0] = func4

f = b[0]()
