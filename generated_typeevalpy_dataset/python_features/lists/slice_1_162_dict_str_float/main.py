# A new list is created as a slice of another one containing functions.


def func1():
    return {'truxn': 88, 'ewsrv': 69, 'hknwm': 69}


def func2():
    return 'kbacu'


def func3():
    return 68.84


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
