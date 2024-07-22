# Functions are assigned as elements of a list and then called.


def func1():
    return [49, 17, 9]


def func2():
    return 15.81


def func3():
    return (2, 94, 90)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'cfqro': 72, 'cqhsn': 66, 'uyqrg': 68}


b = ["Hello"]
b[0] = func4

f = b[0]()
