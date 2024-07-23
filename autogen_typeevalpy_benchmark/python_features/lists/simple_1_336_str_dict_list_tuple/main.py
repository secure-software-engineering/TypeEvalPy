# Functions are assigned as elements of a list and then called.


def func1():
    return 'tuawg'


def func2():
    return {'vezbg': 81, 'ulard': 37, 'bgtez': 65}


def func3():
    return [86, 7, 90]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (8, 36, 8)


b = ["Hello"]
b[0] = func4

f = b[0]()
