# A new list is created as a slice of another one containing functions.


def func1():
    return False


def func2():
    return 65.31


def func3():
    return {'qrhwd': 42, 'jbohw': 36, 'fnabp': 27}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
