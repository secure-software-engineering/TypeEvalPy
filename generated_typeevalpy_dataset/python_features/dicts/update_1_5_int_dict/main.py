# The update method of dictionaries is used.


def func1():
    return {'mvqyw': 15, 'tiqhd': 28, 'fesbl': 31}


def func2():
    return 59


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
