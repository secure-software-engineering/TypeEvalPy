# The update method of dictionaries is used.


def func1():
    return (87, 20, 21)


def func2():
    return {'dnaqw': 100, 'rarkg': 18, 'lqrnv': 6}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
