# Functions are assigned as elements of a list and then called.


def func1():
    return {'xgcam': 73, 'seycw': 93, 'qvelk': 28}


def func2():
    return [44, 27, 50]


def func3():
    return (9, 84, 33)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
