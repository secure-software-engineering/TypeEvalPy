# A dictionary key is assigned to a function.


def func1():
    return 'ufvea'


def func2():
    return (98, 53, 91)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
