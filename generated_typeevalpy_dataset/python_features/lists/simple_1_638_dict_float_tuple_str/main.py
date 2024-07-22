# Functions are assigned as elements of a list and then called.


def func1():
    return {'yaowf': 41, 'snhux': 78, 'hilxv': 50}


def func2():
    return 15.88


def func3():
    return (81, 73, 93)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'cjhny'


b = ["Hello"]
b[0] = func4

f = b[0]()
