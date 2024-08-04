# Functions are assigned as elements of a list and then called.


def func1():
    return {'jsfor': 24, 'sojjt': 62, 'yuyws': 6}


def func2():
    return [76, 66, 31]


def func3():
    return 60.63


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
