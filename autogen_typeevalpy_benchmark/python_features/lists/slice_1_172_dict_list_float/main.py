# A new list is created as a slice of another one containing functions.


def func1():
    return {'fziqf': 75, 'btenp': 9, 'vrmff': 32}


def func2():
    return [18, 68, 40]


def func3():
    return 76.07


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
