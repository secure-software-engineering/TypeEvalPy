# Functions are assigned as elements of a list and then called.


def func1():
    return {'kdzsn': 47, 'zejjm': 70, 'ryjne': 45}


def func2():
    return [57, 75, 67]


def func3():
    return 49


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (85, 39, 77)


b = ["Hello"]
b[0] = func4

f = b[0]()
