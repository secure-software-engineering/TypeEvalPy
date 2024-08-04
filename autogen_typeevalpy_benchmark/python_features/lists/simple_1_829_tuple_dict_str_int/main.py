# Functions are assigned as elements of a list and then called.


def func1():
    return (100, 54, 70)


def func2():
    return {'uymzx': 3, 'cowqq': 56, 'ambyo': 54}


def func3():
    return 'xjbij'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 48


b = ["Hello"]
b[0] = func4

f = b[0]()
