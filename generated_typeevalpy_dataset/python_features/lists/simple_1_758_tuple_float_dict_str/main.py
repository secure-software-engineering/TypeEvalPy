# Functions are assigned as elements of a list and then called.


def func1():
    return (16, 90, 38)


def func2():
    return 75.33


def func3():
    return {'hniov': 92, 'lkjwx': 95, 'vuimu': 80}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 'ugvsn'


b = ["Hello"]
b[0] = func4

f = b[0]()
