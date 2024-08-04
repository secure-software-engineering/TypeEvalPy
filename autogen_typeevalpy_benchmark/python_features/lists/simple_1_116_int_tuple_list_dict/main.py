# Functions are assigned as elements of a list and then called.


def func1():
    return 44


def func2():
    return (20, 36, 36)


def func3():
    return [71, 56, 36]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ubvfx': 20, 'orfjt': 77, 'vhyjf': 92}


b = ["Hello"]
b[0] = func4

f = b[0]()
