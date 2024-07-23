# Functions are assigned as elements of a list and then called.


def func1():
    return (70, 78, 28)


def func2():
    return 71


def func3():
    return {'cfufs': 14, 'seqen': 85, 'dqslt': 34}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 19.05


b = ["Hello"]
b[0] = func4

f = b[0]()
