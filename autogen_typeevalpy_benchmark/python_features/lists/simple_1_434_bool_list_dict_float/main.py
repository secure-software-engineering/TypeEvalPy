# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return [72, 90, 58]


def func3():
    return {'wuglh': 50, 'traip': 84, 'bjawl': 59}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 45.37


b = ["Hello"]
b[0] = func4

f = b[0]()
