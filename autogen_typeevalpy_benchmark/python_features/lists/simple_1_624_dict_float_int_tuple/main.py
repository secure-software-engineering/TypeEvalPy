# Functions are assigned as elements of a list and then called.


def func1():
    return {'hdabs': 12, 'miqln': 42, 'vtrlg': 67}


def func2():
    return 23.03


def func3():
    return 96


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (71, 81, 56)


b = ["Hello"]
b[0] = func4

f = b[0]()
