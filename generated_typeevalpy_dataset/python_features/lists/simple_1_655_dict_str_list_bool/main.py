# Functions are assigned as elements of a list and then called.


def func1():
    return {'pkcis': 39, 'jhynk': 7, 'ifvyt': 30}


def func2():
    return 'mwjla'


def func3():
    return [38, 98, 55]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
