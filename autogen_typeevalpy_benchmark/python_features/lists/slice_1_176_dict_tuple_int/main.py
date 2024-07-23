# A new list is created as a slice of another one containing functions.


def func1():
    return {'mxqvb': 27, 'wyeqm': 85, 'yarcs': 88}


def func2():
    return (32, 66, 74)


def func3():
    return 46


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
