# The update method of dictionaries is used.


def func1():
    return 57.41


def func2():
    return {'oeexn': 59, 'ktvzm': 3, 'eabqa': 11}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
