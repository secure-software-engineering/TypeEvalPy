# A new list is created as a slice of another one containing functions.


def func1():
    return {'nkiho': 53, 'lwypk': 45, 'rzyda': 24}


def func2():
    return [64, 91, 92]


def func3():
    return (80, 6, 31)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
