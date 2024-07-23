# Functions are assigned as elements of a list and then called.


def func1():
    return 52


def func2():
    return {'hzzwj': 72, 'gujfj': 25, 'djevk': 36}


def func3():
    return [63, 57, 43]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'bfwtq'


b = ["Hello"]
b[0] = func4

f = b[0]()
