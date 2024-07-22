# A new list is created as a slice of another one containing functions.


def func1():
    return 8.74


def func2():
    return {'trltb': 23, 'klyks': 42, 'ptskh': 93}


def func3():
    return 'zmexm'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
