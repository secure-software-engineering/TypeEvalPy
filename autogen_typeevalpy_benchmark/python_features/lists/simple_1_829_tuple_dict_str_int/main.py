# Functions are assigned as elements of a list and then called.


def func1():
    return (28, 77, 55)


def func2():
    return {'pqjkc': 12, 'binde': 97, 'hwyzw': 79}


def func3():
    return 'khfan'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 4


b = ["Hello"]
b[0] = func4

f = b[0]()
