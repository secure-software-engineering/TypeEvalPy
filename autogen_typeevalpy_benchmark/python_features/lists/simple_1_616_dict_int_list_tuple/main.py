# Functions are assigned as elements of a list and then called.


def func1():
    return {'ieaur': 37, 'tqzcy': 13, 'csstt': 63}


def func2():
    return 8


def func3():
    return [7, 8, 29]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (29, 57, 76)


b = ["Hello"]
b[0] = func4

f = b[0]()
