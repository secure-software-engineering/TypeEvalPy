# Check if tool type coerces integer and string values.


def func1():
    return 68


def func2():
    return {'cuzuk': 22, 'umycf': 63, 'sxohq': 4}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
