# A new list is created as a slice of another one containing functions.


def func1():
    return 30.41


def func2():
    return True


def func3():
    return {'dfped': 26, 'nyqqr': 91, 'otinw': 37}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
