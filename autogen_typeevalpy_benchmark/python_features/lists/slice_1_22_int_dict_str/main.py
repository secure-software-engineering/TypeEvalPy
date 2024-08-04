# A new list is created as a slice of another one containing functions.


def func1():
    return 12


def func2():
    return {'vnhio': 35, 'yqdkd': 80, 'jvwmc': 87}


def func3():
    return 'wvlcs'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
