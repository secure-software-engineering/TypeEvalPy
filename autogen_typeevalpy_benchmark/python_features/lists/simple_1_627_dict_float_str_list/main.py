# Functions are assigned as elements of a list and then called.


def func1():
    return {'veiwb': 84, 'cgkfj': 28, 'iuwgt': 2}


def func2():
    return 35.43


def func3():
    return 'cxxcd'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [84, 90, 32]


b = ["Hello"]
b[0] = func4

f = b[0]()
