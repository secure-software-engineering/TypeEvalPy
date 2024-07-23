# A new list is created as a slice of another one containing functions.


def func1():
    return {'tzcrb': 85, 'jmdsp': 27, 'qywsl': 38}


def func2():
    return True


def func3():
    return (78, 82, 91)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
