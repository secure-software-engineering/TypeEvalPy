# Functions are assigned as elements of a list and then called.


def func1():
    return {'myrli': 12, 'tkobz': 26, 'zfpdh': 96}


def func2():
    return [26, 63, 27]


def func3():
    return (25, 23, 51)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 85


b = ["Hello"]
b[0] = func4

f = b[0]()
