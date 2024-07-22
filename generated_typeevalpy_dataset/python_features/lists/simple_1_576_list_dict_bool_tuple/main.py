# Functions are assigned as elements of a list and then called.


def func1():
    return [99, 84, 36]


def func2():
    return {'xlyai': 59, 'uhgjf': 45, 'cwzxm': 76}


def func3():
    return True


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return (19, 83, 91)


b = ["Hello"]
b[0] = func4

f = b[0]()
