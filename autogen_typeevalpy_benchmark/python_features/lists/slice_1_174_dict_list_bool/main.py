# A new list is created as a slice of another one containing functions.


def func1():
    return {'wdend': 5, 'fjyya': 80, 'psevn': 67}


def func2():
    return [30, 45, 33]


def func3():
    return True


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
