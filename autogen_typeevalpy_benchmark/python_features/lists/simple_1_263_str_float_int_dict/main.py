# Functions are assigned as elements of a list and then called.


def func1():
    return 'tbznq'


def func2():
    return 59.26


def func3():
    return 88


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'zrljy': 84, 'akiak': 94, 'zbsdb': 86}


b = ["Hello"]
b[0] = func4

f = b[0]()
