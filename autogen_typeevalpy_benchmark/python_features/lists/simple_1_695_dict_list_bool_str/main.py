# Functions are assigned as elements of a list and then called.


def func1():
    return {'qfbud': 36, 'tmtwc': 99, 'nooor': 99}


def func2():
    return [92, 88, 35]


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'vlsbn'


b = ["Hello"]
b[0] = func4

f = b[0]()
