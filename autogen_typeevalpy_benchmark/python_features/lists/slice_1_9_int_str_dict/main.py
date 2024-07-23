# A new list is created as a slice of another one containing functions.


def func1():
    return 43


def func2():
    return 'ziglm'


def func3():
    return {'hoaou': 78, 'ujjur': 9, 'juryw': 69}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
