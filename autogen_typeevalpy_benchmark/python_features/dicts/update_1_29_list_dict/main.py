# The update method of dictionaries is used.


def func1():
    return {'sdkhp': 84, 'rburv': 6, 'pbmir': 24}


def func2():
    return [47, 27, 3]


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
