# Functions are assigned as elements of a list and then called.


def func1():
    return [67, 6, 81]


def func2():
    return 63.05


def func3():
    return {'yqkke': 48, 'hpakw': 96, 'xfpkw': 42}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'mzwog'


b = ["Hello"]
b[0] = func4

f = b[0]()
