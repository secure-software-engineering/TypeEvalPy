# A new list is created as a slice of another one containing functions.


def func1():
    return (20, 65, 37)


def func2():
    return 55.94


def func3():
    return {'uyxdm': 25, 'mmntf': 31, 'trjgy': 30}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
