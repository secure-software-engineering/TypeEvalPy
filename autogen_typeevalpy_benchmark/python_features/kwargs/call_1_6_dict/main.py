# Call a function with keyword arguments.


def func1():
    return {'fmxna': 39, 'qfbmb': 45, 'qmomc': 14}


def func(a):
    return a()


c = func(a=func1)
