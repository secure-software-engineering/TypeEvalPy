# A new list is created as a slice of another one containing functions.


def func1():
    return [42, 68, 45]


def func2():
    return 'dufmp'


def func3():
    return {'ilpjb': 98, 'ehsre': 72, 'bnwus': 87}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
