# Functions are assigned as elements of a list and then called.


def func1():
    return 'yhaxk'


def func2():
    return False


def func3():
    return (15, 84, 72)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 83.78


b = ["Hello"]
b[0] = func4

f = b[0]()
