# Functions are assigned as elements of a list and then called.


def func1():
    return (94, 30, 19)


def func2():
    return {'nkevz': 14, 'mdxgy': 18, 'ponud': 52}


def func3():
    return [84, 3, 89]


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 54.83


b = ["Hello"]
b[0] = func4

f = b[0]()
