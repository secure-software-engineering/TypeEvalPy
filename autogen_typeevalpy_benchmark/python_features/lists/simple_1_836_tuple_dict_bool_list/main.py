# Functions are assigned as elements of a list and then called.


def func1():
    return (45, 62, 97)


def func2():
    return {'vnisv': 92, 'syumw': 39, 'funkh': 51}


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [100, 46, 47]


b = ["Hello"]
b[0] = func4

f = b[0]()
