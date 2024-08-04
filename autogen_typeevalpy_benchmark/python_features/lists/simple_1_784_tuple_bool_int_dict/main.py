# Functions are assigned as elements of a list and then called.


def func1():
    return (17, 80, 93)


def func2():
    return False


def func3():
    return 78


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'hnkwr': 89, 'byvst': 51, 'wvufg': 78}


b = ["Hello"]
b[0] = func4

f = b[0]()
