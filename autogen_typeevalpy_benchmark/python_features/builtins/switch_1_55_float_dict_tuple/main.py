#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 80.43:
            return {'twjvn': 86, 'hglcx': 63, 'jwlxc': 78}
        case {'twjvn': 86, 'hglcx': 63, 'jwlxc': 78}:
            return 80.43
        case _:
            return "default"


a = func(80.43)
b = func({'twjvn': 86, 'hglcx': 63, 'jwlxc': 78})
c = func((30, 84, 66))
