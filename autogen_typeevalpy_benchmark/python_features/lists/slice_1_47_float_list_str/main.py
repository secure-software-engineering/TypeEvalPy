# A new list is created as a slice of another one containing functions.


def func1():
    return 84.92


def func2():
    return [29, 88, 49]


def func3():
    return 'ntmze'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
