# A new list is created as a slice of another one containing functions.


def func1():
    return [97, 50, 73]


def func2():
    return {'lenyu': 71, 'nqnag': 46, 'wfoxu': 81}


def func3():
    return (58, 90, 28)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
