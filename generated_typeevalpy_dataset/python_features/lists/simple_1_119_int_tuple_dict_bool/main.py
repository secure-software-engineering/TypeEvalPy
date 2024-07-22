# Functions are assigned as elements of a list and then called.


def func1():
    return 82


def func2():
    return (11, 48, 27)


def func3():
    return {'edlcl': 49, 'yprae': 76, 'klniu': 48}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
