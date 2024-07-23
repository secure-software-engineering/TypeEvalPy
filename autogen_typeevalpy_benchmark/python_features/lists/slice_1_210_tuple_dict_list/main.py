# A new list is created as a slice of another one containing functions.


def func1():
    return (10, 36, 85)


def func2():
    return {'flnav': 60, 'ybohc': 68, 'iujys': 90}


def func3():
    return [86, 2, 35]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
