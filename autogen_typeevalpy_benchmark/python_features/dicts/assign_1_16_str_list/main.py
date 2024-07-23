# A dictionary key is assigned to a function.


def func1():
    return 'hidud'


def func2():
    return [76, 9, 4]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
