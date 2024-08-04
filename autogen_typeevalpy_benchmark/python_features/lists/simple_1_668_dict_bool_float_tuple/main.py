# Functions are assigned as elements of a list and then called.


def func1():
    return {'lqbtf': 37, 'gtbbm': 96, 'nljrj': 43}


def func2():
    return True


def func3():
    return 21.29


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (71, 89, 100)


b = ["Hello"]
b[0] = func4

f = b[0]()
