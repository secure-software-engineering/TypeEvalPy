# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return {'elpqm': 38, 'iwyxo': 80, 'dxbsm': 13}


def func3():
    return (37, 83, 16)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
