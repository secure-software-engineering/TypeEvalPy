# Functions are assigned as elements of a list and then called.


def func1():
    return 76.84


def func2():
    return {'kdxcq': 17, 'ltiyw': 20, 'cgrvg': 62}


def func3():
    return [4, 92, 7]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
