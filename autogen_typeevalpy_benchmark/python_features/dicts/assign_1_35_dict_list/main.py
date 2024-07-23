# A dictionary key is assigned to a function.


def func1():
    return {'cdoon': 98, 'sgjaf': 30, 'vcjbw': 74}


def func2():
    return [16, 73, 16]


d = {"a": func1}

d["a"] = func2

e = d["a"]()
