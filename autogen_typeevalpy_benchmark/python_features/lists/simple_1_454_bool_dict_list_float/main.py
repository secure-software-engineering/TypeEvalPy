# Functions are assigned as elements of a list and then called.


def func1():
    return False


def func2():
    return {'jvcfu': 3, 'seyyw': 91, 'bjbac': 90}


def func3():
    return [47, 4, 74]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 92.74


b = ["Hello"]
b[0] = func4

f = b[0]()
