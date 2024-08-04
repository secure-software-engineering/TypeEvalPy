# A dictionary key is assigned to a function.


def func1():
    return [73, 84, 72]


def func2():
    return 'xcpaw'


d = {"a": func1}

d["a"] = func2

e = d["a"]()
