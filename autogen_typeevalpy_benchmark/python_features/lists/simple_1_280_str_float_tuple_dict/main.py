# Functions are assigned as elements of a list and then called.


def func1():
    return 'fwrkh'


def func2():
    return 65.35


def func3():
    return (75, 62, 89)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'vwwmt': 54, 'ecsva': 71, 'xspnc': 48}


b = ["Hello"]
b[0] = func4

f = b[0]()
