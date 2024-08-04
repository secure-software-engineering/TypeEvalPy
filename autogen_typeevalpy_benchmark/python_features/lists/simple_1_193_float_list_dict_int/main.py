# Functions are assigned as elements of a list and then called.


def func1():
    return 13.39


def func2():
    return [19, 18, 10]


def func3():
    return {'xzuqn': 73, 'ofdbj': 90, 'pboqg': 20}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 84


b = ["Hello"]
b[0] = func4

f = b[0]()
