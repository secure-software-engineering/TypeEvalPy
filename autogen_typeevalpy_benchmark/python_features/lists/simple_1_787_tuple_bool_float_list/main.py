# Functions are assigned as elements of a list and then called.


def func1():
    return (79, 18, 36)


def func2():
    return False


def func3():
    return 31.14


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [93, 59, 56]


b = ["Hello"]
b[0] = func4

f = b[0]()
