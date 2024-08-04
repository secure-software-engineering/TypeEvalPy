# A new list is created as a slice of another one containing functions.


def func1():
    return (58, 51, 46)


def func2():
    return False


def func3():
    return {'oytjc': 73, 'ffhhy': 50, 'lttgs': 53}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
