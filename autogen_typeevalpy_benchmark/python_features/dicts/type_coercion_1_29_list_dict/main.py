# Check if tool type coerces integer and string values.


def func1():
    return [56, 68, 92]


def func2():
    return {'htyrz': 8, 'seacf': 38, 'gclxr': 63}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
