# Functions are assigned as elements of a list and then called.


def func1():
    return {'uanss': 26, 'txrtb': 86, 'spyxc': 58}


def func2():
    return (3, 70, 61)


def func3():
    return 100


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [34, 31, 57]


b = ["Hello"]
b[0] = func4

f = b[0]()
