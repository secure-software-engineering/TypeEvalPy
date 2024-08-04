# A new list is created as a slice of another one containing functions.


def func1():
    return {'rztaq': 85, 'dltav': 89, 'hwvkp': 64}


def func2():
    return (61, 88, 83)


def func3():
    return 'medoe'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
