# Functions are assigned as elements of a list and then called.


def func1():
    return 45


def func2():
    return {'nrsuj': 72, 'qyghc': 70, 'wbnvh': 31}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [78, 97, 24]


b = ["Hello"]
b[0] = func4

f = b[0]()
