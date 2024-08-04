# A new list is created as a slice of another one containing functions.


def func1():
    return 79.61


def func2():
    return {'smylx': 3, 'qbbxd': 80, 'nmhly': 4}


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
