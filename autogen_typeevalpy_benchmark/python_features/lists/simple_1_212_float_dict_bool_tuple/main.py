# Functions are assigned as elements of a list and then called.


def func1():
    return 13.7


def func2():
    return {'ntmer': 92, 'olsbx': 51, 'wqxoi': 34}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (72, 70, 2)


b = ["Hello"]
b[0] = func4

f = b[0]()
