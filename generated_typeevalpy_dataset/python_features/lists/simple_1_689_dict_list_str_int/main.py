# Functions are assigned as elements of a list and then called.


def func1():
    return {'nqkic': 19, 'naxst': 97, 'ydwll': 76}


def func2():
    return [75, 63, 84]


def func3():
    return 'exyzg'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 73


b = ["Hello"]
b[0] = func4

f = b[0]()
