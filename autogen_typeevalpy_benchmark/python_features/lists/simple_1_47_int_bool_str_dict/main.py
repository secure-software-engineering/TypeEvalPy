# Functions are assigned as elements of a list and then called.


def func1():
    return 96


def func2():
    return False


def func3():
    return 'okhcs'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'edogn': 14, 'dqryc': 12, 'ienzf': 71}


b = ["Hello"]
b[0] = func4

f = b[0]()
