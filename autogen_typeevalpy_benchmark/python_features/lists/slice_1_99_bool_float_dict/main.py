# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return 37.08


def func3():
    return {'fdpqk': 47, 'lxdum': 67, 'buaob': 66}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
