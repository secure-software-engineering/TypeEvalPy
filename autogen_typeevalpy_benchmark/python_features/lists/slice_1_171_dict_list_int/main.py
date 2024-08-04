# A new list is created as a slice of another one containing functions.


def func1():
    return {'xfjcs': 72, 'zmnla': 28, 'tepme': 23}


def func2():
    return [73, 33, 67]


def func3():
    return 3


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
