# A dictionary is returned.


def func2():
    return {'gxlrz': 82, 'uehst': 60, 'gokvj': 95}


def func1():
    d = {"a": func2}
    return d


b = func1()
c = b["a"]()
