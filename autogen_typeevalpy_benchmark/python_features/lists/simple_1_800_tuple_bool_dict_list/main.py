# Functions are assigned as elements of a list and then called.


def func1():
    return (38, 91, 38)


def func2():
    return True


def func3():
    return {'ihkks': 4, 'dfagz': 30, 'helbt': 57}


a = [func1, func2, func3]

c = a[0]()
d = a[1]()
e = a[2]()


def func4():
    return [47, 35, 15]


b = ["Hello"]
b[0] = func4

f = b[0]()
