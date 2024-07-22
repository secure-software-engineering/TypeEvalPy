# Functions are assigned as elements of a list and then called.


def func1():
    return {'faqvt': 33, 'ixtnz': 32, 'ulxcg': 63}


def func2():
    return [78, 36, 20]


def func3():
    return 'xljoa'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 89.19


b = ["Hello"]
b[0] = func4

f = b[0]()
