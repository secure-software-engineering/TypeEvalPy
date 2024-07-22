# Functions are assigned as elements of a list and then called.


def func1():
    return 1


def func2():
    return [49, 28, 100]


def func3():
    return {'hxgsp': 15, 'sduac': 49, 'mrjql': 55}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (23, 86, 68)


b = ["Hello"]
b[0] = func4

f = b[0]()
