# Functions are assigned as elements of a list and then called.


def func1():
    return {'zeaub': 61, 'igtuj': 3, 'bbycv': 12}


def func2():
    return (94, 15, 94)


def func3():
    return 'xpeqs'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return True


b = ["Hello"]
b[0] = func4

f = b[0]()
