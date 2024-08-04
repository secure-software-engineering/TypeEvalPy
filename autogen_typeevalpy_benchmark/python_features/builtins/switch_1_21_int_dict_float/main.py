#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 21:
            return {'jhyxh': 32, 'zaedf': 73, 'suqsd': 37}
        case {'jhyxh': 32, 'zaedf': 73, 'suqsd': 37}:
            return 21
        case _:
            return "default"


a = func(21)
b = func({'jhyxh': 32, 'zaedf': 73, 'suqsd': 37})
c = func(1.39)
