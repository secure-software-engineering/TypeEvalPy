# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return 'mptgy'


def func3():
    return {'qichy': 3, 'klweh': 14, 'gerhh': 21}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (10, 57, 72)


b = ["Hello"]
b[0] = func4

f = b[0]()
