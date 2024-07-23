# Check if tool type coerces integer and string values.


def func1():
    return {'cwmpf': 67, 'ouskr': 17, 'pvkkc': 25}


def func2():
    return (98, 43, 64)


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
