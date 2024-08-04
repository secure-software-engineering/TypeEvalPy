# A new list is created as a slice of another one containing functions.


def func1():
    return 'kjcul'


def func2():
    return (87, 13, 82)


def func3():
    return {'aurnv': 98, 'fclyd': 79, 'nablu': 70}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
