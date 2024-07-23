# Functions are assigned as elements of a list and then called.


def func1():
    return [17, 18, 57]


def func2():
    return {'zudaq': 47, 'isxyj': 70, 'ffese': 38}


def func3():
    return (100, 58, 92)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 62


b = ["Hello"]
b[0] = func4

f = b[0]()
