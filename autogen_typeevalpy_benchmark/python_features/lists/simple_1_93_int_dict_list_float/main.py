# Functions are assigned as elements of a list and then called.


def func1():
    return 40


def func2():
    return {'cckum': 2, 'rstgh': 36, 'hcsmb': 33}


def func3():
    return [45, 49, 63]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 3.0


b = ["Hello"]
b[0] = func4

f = b[0]()
