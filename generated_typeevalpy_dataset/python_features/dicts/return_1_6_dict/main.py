# A dictionary is returned.


def func2():
    return {'kmvzp': 23, 'uphlw': 24, 'mzocs': 17}


def func1():
    d = {"a": func2}
    return d


b = func1()
c = b["a"]()
