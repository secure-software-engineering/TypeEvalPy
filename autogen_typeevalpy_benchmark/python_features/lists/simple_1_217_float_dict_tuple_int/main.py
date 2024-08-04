# Functions are assigned as elements of a list and then called.


def func1():
    return 5.99


def func2():
    return {'xzbrv': 75, 'ugqlg': 67, 'lrmjn': 57}


def func3():
    return (63, 12, 94)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 94


b = ["Hello"]
b[0] = func4

f = b[0]()
