# Functions are assigned as elements of a list and then called.


def func1():
    return {'mcvlo': 78, 'mjfja': 37, 'huizi': 18}


def func2():
    return (64, 48, 30)


def func3():
    return 'mlekx'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 74


b = ["Hello"]
b[0] = func4

f = b[0]()
