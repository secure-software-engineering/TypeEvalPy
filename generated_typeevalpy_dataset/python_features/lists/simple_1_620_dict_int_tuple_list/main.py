# Functions are assigned as elements of a list and then called.


def func1():
    return {'qoefn': 73, 'cemin': 98, 'dowif': 94}


def func2():
    return 14


def func3():
    return (54, 60, 84)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [76, 57, 95]


b = ["Hello"]
b[0] = func4

f = b[0]()
