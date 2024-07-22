# Functions are assigned as elements of a list and then called.


def func1():
    return {'ycjlb': 14, 'rwqms': 87, 'ckfwz': 60}


def func2():
    return (6, 17, 50)


def func3():
    return 'hzxmk'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return False


b = ["Hello"]
b[0] = func4

f = b[0]()
