# Functions are assigned as elements of a list and then called.


def func1():
    return 39.5


def func2():
    return [75, 29, 60]


def func3():
    return {'bmilh': 24, 'fcneb': 3, 'sxiys': 45}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (48, 41, 30)


b = ["Hello"]
b[0] = func4

f = b[0]()
