# Functions are assigned as elements of a list and then called.


def func1():
    return 'vvknq'


def func2():
    return {'pknyf': 84, 'krhyq': 81, 'ryrdf': 68}


def func3():
    return (29, 23, 11)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 52


b = ["Hello"]
b[0] = func4

f = b[0]()
