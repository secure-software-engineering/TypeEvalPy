# Functions are assigned as elements of a list and then called.


def func1():
    return (2, 63, 87)


def func2():
    return 25


def func3():
    return [91, 54, 97]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'fqqmj': 94, 'elrdx': 11, 'aowsr': 34}


b = ["Hello"]
b[0] = func4

f = b[0]()
