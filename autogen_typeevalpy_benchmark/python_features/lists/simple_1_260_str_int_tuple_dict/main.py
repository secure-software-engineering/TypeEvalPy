# Functions are assigned as elements of a list and then called.


def func1():
    return 'wsizb'


def func2():
    return 42


def func3():
    return (55, 47, 20)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'mbcqv': 20, 'zekto': 4, 'cbjlv': 6}


b = ["Hello"]
b[0] = func4

f = b[0]()
