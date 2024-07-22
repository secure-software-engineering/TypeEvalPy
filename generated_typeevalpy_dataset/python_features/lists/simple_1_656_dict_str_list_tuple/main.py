# Functions are assigned as elements of a list and then called.


def func1():
    return {'bubcn': 32, 'pjmbt': 35, 'kixlp': 74}


def func2():
    return 'sseqq'


def func3():
    return [76, 100, 66]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (4, 18, 8)


b = ["Hello"]
b[0] = func4

f = b[0]()
