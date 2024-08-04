# Functions are assigned as elements of a list and then called.


def func1():
    return [80, 36, 9]


def func2():
    return {'wjnrl': 49, 'jjdyg': 12, 'tnozx': 19}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'xrtma'


b = ["Hello"]
b[0] = func4

f = b[0]()
