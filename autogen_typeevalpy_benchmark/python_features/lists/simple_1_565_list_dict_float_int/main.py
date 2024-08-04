# Functions are assigned as elements of a list and then called.


def func1():
    return [93, 38, 7]


def func2():
    return {'uhnyo': 28, 'vggqu': 78, 'xsjix': 62}


def func3():
    return 8.87


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return 65


b = ["Hello"]
b[0] = func4

f = b[0]()
