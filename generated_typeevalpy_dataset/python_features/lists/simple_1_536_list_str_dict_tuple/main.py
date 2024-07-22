# Functions are assigned as elements of a list and then called.


def func1():
    return [41, 82, 70]


def func2():
    return 'ztade'


def func3():
    return {'dmpuh': 64, 'grqeh': 5, 'anvmq': 81}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (23, 43, 4)


b = ["Hello"]
b[0] = func4

f = b[0]()
