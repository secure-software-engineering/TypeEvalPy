# Functions are assigned as elements of a list and then called.


def func1():
    return [3, 78, 62]


def func2():
    return (7, 55, 35)


def func3():
    return {'yzbzm': 34, 'zqrfh': 81, 'kcvii': 4}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'uyore'


b = ["Hello"]
b[0] = func4

f = b[0]()
