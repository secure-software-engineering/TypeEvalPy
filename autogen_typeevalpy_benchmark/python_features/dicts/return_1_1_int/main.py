# A dictionary is returned.


def func2():
    return 35


def func1():
    d = {"a": func2}
    return d


b = func1()
c = b["a"]()
