# Functions are assigned as elements of a list and then called.


def func1():
    return 94.64


def func2():
    return (87, 88, 70)


def func3():
    return [74, 32, 29]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'xjccd': 81, 'ddvak': 81, 'vlmqa': 69}


b = ["Hello"]
b[0] = func4

f = b[0]()
