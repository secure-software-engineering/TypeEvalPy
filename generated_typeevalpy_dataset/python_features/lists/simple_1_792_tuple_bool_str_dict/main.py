# Functions are assigned as elements of a list and then called.


def func1():
    return (59, 44, 59)


def func2():
    return True


def func3():
    return 'lthpv'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'ixxsz': 15, 'knimr': 81, 'fodqz': 27}


b = ["Hello"]
b[0] = func4

f = b[0]()
