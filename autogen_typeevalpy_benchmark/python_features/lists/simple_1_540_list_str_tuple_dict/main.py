# Functions are assigned as elements of a list and then called.


def func1():
    return [51, 92, 27]


def func2():
    return 'jpydp'


def func3():
    return (69, 61, 3)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'rqlfv': 63, 'xdfqa': 21, 'cysui': 35}


b = ["Hello"]
b[0] = func4

f = b[0]()
