# Functions are assigned as elements of a list and then called.


def func1():
    return [77, 20, 79]


def func2():
    return (57, 62, 5)


def func3():
    return 'equho'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'iihea': 88, 'hzsle': 73, 'uucpr': 52}


b = ["Hello"]
b[0] = func4

f = b[0]()
