# Check if tool type coerces integer and string values.


def func1():
    return 'lscun'


def func2():
    return {'hsgki': 85, 'vmmcd': 59, 'ckcox': 54}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
