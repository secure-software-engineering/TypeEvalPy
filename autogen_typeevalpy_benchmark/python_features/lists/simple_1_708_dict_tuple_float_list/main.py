# Functions are assigned as elements of a list and then called.


def func1():
    return {'pwnwq': 83, 'hdryz': 25, 'tkxzt': 90}


def func2():
    return (25, 64, 38)


def func3():
    return 48.78


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [12, 14, 80]


b = ["Hello"]
b[0] = func4

f = b[0]()
