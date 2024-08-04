# Functions are assigned as elements of a list and then called.


def func1():
    return (79, 5, 56)


def func2():
    return [50, 4, 30]


def func3():
    return {'kgpct': 23, 'wckfg': 69, 'xfjhu': 4}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 27.61


b = ["Hello"]
b[0] = func4

f = b[0]()
