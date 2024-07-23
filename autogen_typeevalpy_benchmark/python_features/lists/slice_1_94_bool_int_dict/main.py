# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return 66


def func3():
    return {'uvqor': 43, 'yonag': 98, 'ryrpp': 25}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
