# A new list is created as a slice of another one containing functions.


def func1():
    return {'rqeiw': 2, 'wycth': 70, 'dqvfk': 35}


def func2():
    return 'uivuh'


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
