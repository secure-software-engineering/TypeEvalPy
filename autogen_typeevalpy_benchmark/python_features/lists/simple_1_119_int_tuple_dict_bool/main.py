# Functions are assigned as elements of a list and then called.


def func1():
    return 78


def func2():
    return (22, 91, 38)


def func3():
    return {'ztdux': 47, 'fwlwt': 15, 'cfyre': 54}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
