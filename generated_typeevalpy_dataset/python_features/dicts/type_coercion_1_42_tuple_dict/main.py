# Check if tool type coerces integer and string values.


def func1():
    return (35, 32, 82)


def func2():
    return {'krpuy': 25, 'urevz': 22, 'spnjk': 69}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
