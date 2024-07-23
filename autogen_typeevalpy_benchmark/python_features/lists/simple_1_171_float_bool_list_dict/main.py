# Functions are assigned as elements of a list and then called.


def func1():
    return 95.97


def func2():
    return False


def func3():
    return [59, 12, 69]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'imujn': 17, 'bzodc': 11, 'ryqlc': 66}


b = ["Hello"]
b[0] = func4

f = b[0]()
