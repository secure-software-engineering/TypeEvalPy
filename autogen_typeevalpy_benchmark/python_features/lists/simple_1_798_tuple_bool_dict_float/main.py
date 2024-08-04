# Functions are assigned as elements of a list and then called.


def func1():
    return (79, 72, 70)


def func2():
    return True


def func3():
    return {'aovod': 19, 'zfzrw': 85, 'wzndh': 17}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 23.54


b = ["Hello"]
b[0] = func4

f = b[0]()
