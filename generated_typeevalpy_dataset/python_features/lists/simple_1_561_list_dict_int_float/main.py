# Functions are assigned as elements of a list and then called.


def func1():
    return [93, 88, 65]


def func2():
    return {'fnuau': 15, 'zevmx': 64, 'qlmbl': 35}


def func3():
    return 34


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 14.5


b = ["Hello"]
b[0] = func4

f = b[0]()
