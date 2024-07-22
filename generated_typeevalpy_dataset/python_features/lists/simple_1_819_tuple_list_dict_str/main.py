# Functions are assigned as elements of a list and then called.


def func1():
    return (48, 56, 9)


def func2():
    return [69, 68, 20]


def func3():
    return {'vchdj': 33, 'wxbmf': 18, 'xvgnz': 37}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'bmxam'


b = ["Hello"]
b[0] = func4

f = b[0]()
