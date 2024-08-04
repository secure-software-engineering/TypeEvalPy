# Functions are assigned as elements of a list and then called.


def func1():
    return 95.17


def func2():
    return True


def func3():
    return {'scxvw': 6, 'gbbwa': 40, 'rgave': 75}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [44, 50, 54]


b = ["Hello"]
b[0] = func4

f = b[0]()
