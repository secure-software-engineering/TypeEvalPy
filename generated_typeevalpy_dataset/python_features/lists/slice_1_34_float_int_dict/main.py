# A new list is created as a slice of another one containing functions.


def func1():
    return 32.27


def func2():
    return 68


def func3():
    return {'rsqyg': 65, 'enlpz': 92, 'bkact': 85}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
