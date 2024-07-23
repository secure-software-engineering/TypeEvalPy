# Functions are assigned as elements of a list and then called.


def func1():
    return 14.83


def func2():
    return 6


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'qncym': 20, 'zkqbz': 35, 'vqyok': 12}


b = ["Hello"]
b[0] = func4

f = b[0]()
