# A dictionary is returned.


def func2():
    return 'ieyqp'


def func1():
    d = {"a": func2}
    return d


b = func1()
c = b["a"]()