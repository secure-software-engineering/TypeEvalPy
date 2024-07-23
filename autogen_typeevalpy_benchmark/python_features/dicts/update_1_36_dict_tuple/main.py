# The update method of dictionaries is used.


def func1():
    return (15, 9, 72)


def func2():
    return {'kiodb': 19, 'azzaq': 77, 'yizkd': 15}


d = {"a": func1}

d.update({"a": func2})
e = d["a"]()
