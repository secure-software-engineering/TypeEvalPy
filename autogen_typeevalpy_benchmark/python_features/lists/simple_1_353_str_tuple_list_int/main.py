# Functions are assigned as elements of a list and then called.


def func1():
    return 'npgzv'


def func2():
    return (97, 96, 93)


def func3():
    return [51, 43, 55]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 4


b = ["Hello"]
b[0] = func4

f = b[0]()
