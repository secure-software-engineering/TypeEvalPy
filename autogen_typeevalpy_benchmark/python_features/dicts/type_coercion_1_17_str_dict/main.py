# Check if tool type coerces integer and string values.


def func1():
    return 'kyeuo'


def func2():
    return {'gpzoz': 4, 'bamct': 86, 'zavbk': 58}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
