# The update method of dictionaries is used.


def func1():
    return [95, 71, 23]


def func2():
    return {'yxloz': 61, 'bmequ': 23, 'lrbqe': 19}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
