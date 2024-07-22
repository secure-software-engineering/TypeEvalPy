# Functions are assigned as elements of a list and then called.


def func1():
    return 18


def func2():
    return [25, 84, 83]


def func3():
    return (23, 95, 59)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 93.78


b = ["Hello"]
b[0] = func4

f = b[0]()
