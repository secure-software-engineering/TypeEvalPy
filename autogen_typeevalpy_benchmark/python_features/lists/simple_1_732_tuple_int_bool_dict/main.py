# Functions are assigned as elements of a list and then called.


def func1():
    return (13, 79, 68)


def func2():
    return 73


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'gvlmi': 56, 'usste': 53, 'mzvah': 44}


b = ["Hello"]
b[0] = func4

f = b[0]()
