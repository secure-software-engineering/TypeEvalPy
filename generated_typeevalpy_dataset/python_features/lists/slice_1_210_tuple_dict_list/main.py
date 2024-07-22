# A new list is created as a slice of another one containing functions.


def func1():
    return (9, 95, 77)


def func2():
    return {'gzmib': 39, 'vaarp': 68, 'sfimb': 24}


def func3():
    return [89, 66, 59]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
