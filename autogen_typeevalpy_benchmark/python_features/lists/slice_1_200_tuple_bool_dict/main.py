# A new list is created as a slice of another one containing functions.


def func1():
    return (48, 95, 53)


def func2():
    return False


def func3():
    return {'ecalp': 98, 'rtdla': 28, 'yiodk': 4}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
