# Functions are assigned as elements of a list and then called.


def func1():
    return 96.12


def func2():
    return [75, 20, 94]


def func3():
    return (69, 82, 72)


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return {'tswnn': 41, 'ckryx': 23, 'snhif': 85}


b = ["Hello"]
b[0] = func4

f = b[0]()
