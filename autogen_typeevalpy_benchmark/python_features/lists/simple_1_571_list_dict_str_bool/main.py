# Functions are assigned as elements of a list and then called.


def func1():
    return [40, 87, 27]


def func2():
    return {'fpqmw': 65, 'apvpn': 98, 'lxpid': 59}


def func3():
    return 'cpzsa'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
