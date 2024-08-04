# A new list is created as a slice of another one containing functions.


def func1():
    return (46, 26, 32)


def func2():
    return {'nlfbl': 34, 'qhkzc': 11, 'mlqgp': 35}


def func3():
    return False


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
