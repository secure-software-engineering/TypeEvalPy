# Functions are assigned as elements of a list and then called.


def func1():
    return True


def func2():
    return {'cpyfw': 72, 'wzxns': 48, 'ntwun': 4}


def func3():
    return 'urukg'


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (58, 20, 49)


b = ["Hello"]
b[0] = func4

f = b[0]()