# Functions are assigned as elements of a list and then called.


def func1():
    return 12


def func2():
    return {'fbvqs': 14, 'hoaxc': 46, 'sxvuo': 85}


def func3():
    return [82, 72, 93]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'wpmmd'


b = ["Hello"]
b[0] = func4

f = b[0]()
