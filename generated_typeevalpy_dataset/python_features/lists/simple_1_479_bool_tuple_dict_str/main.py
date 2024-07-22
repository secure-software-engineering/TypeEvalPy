# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return (95, 18, 44)


def func3():
    return {'xfqwh': 3, 'tikle': 5, 'zdbta': 59}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'hgjxr'


b = ["Hello"]
b[0] = func4

f = b[0]()
