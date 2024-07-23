# A new list is created as a slice of another one containing functions.


def func1():
    return 71.58


def func2():
    return {'qvkgt': 42, 'srxhz': 47, 'agqrh': 75}


def func3():
    return 'sbqpu'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
