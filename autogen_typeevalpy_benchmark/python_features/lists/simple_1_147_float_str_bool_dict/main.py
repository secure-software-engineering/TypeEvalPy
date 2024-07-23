# Functions are assigned as elements of a list and then called.


def func1():
    return 33.49


def func2():
    return 'sussf'


def func3():
    return False


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'secic': 93, 'pbhft': 36, 'rpown': 97}


b = ["Hello"]
b[0] = func4

f = b[0]()
