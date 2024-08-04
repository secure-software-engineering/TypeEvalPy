# A new list is created as a slice of another one containing functions.


def func1():
    return {'pyujg': 82, 'vfaxs': 36, 'geoax': 33}


def func2():
    return (32, 17, 74)


def func3():
    return 63


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
