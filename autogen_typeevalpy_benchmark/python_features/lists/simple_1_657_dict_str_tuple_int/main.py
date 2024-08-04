# Functions are assigned as elements of a list and then called.


def func1():
    return {'lbrao': 18, 'wnzvv': 89, 'oyvsy': 19}


def func2():
    return 'oibak'


def func3():
    return (12, 55, 50)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 67


b = ["Hello"]
b[0] = func4

f = b[0]()
