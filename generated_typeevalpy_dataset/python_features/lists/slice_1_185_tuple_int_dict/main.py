# A new list is created as a slice of another one containing functions.


def func1():
    return (5, 81, 83)


def func2():
    return 11


def func3():
    return {'ovusd': 89, 'dpotc': 47, 'lepsr': 84}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
