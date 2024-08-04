# Functions are assigned as elements of a list and then called.


def func1():
    return 27


def func2():
    return (44, 47, 76)


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'kzhqj': 38, 'kfrjg': 34, 'kikal': 27}


b = ["Hello"]
b[0] = func4

f = b[0]()
