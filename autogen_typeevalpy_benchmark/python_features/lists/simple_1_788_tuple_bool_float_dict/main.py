# Functions are assigned as elements of a list and then called.


def func1():
    return (77, 61, 72)


def func2():
    return True


def func3():
    return 43.82


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'analf': 89, 'ebanu': 35, 'nwrxc': 80}


b = ["Hello"]
b[0] = func4

f = b[0]()
