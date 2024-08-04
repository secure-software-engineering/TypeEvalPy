# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return {'updcl': 96, 'cggsn': 87, 'zkjpa': 81}


def func3():
    return [93, 13, 53]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 86


b = ["Hello"]
b[0] = func4

f = b[0]()
