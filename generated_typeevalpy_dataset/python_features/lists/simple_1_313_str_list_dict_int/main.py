# Functions are assigned as elements of a list and then called.


def func1():
    return 'nsreu'


def func2():
    return [68, 12, 3]


def func3():
    return {'hnzyg': 2, 'ozpln': 47, 'krakk': 25}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 22


b = ["Hello"]
b[0] = func4

f = b[0]()
