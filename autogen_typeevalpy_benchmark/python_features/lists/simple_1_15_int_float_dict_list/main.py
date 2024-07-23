# Functions are assigned as elements of a list and then called.


def func1():
    return 32


def func2():
    return 72.46


def func3():
    return {'dmhnu': 93, 'kgtlb': 68, 'ksxgb': 81}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [73, 91, 81]


b = ["Hello"]
b[0] = func4

f = b[0]()
