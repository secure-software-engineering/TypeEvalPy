# Functions are assigned as elements of a list and then called.


def func1():
    return 73


def func2():
    return [52, 85, 81]


def func3():
    return {'vfrsi': 1, 'dpuex': 6, 'wwzmr': 69}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (18, 23, 17)


b = ["Hello"]
b[0] = func4

f = b[0]()
