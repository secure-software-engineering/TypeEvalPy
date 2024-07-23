# Functions are assigned as elements of a list and then called.


def func1():
    return 44


def func2():
    return [14, 2, 17]


def func3():
    return 'hljts'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'vmtvt': 51, 'phuxe': 8, 'zqiyi': 71}


b = ["Hello"]
b[0] = func4

f = b[0]()
