# Functions are assigned as elements of a list and then called.


def func1():
    return {'jksqc': 13, 'tlvxd': 30, 'vyqus': 3}


def func2():
    return 'jodug'


def func3():
    return [96, 22, 40]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (99, 81, 75)


b = ["Hello"]
b[0] = func4

f = b[0]()
