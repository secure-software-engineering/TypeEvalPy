# Functions are assigned as elements of a list and then called.


def func1():
    return (75, 20, 79)


def func2():
    return 7


def func3():
    return 'uubeu'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'vfkdd': 72, 'teauo': 84, 'nqsss': 64}


b = ["Hello"]
b[0] = func4

f = b[0]()
