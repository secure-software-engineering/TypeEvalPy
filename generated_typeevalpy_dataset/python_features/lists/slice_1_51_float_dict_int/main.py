# A new list is created as a slice of another one containing functions.


def func1():
    return 66.79


def func2():
    return {'hunvs': 78, 'nhmpo': 62, 'nwqap': 10}


def func3():
    return 45


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
