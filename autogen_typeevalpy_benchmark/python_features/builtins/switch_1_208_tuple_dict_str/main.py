#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (16, 34, 48):
            return {'zqufh': 10, 'wergi': 4, 'mxeif': 93}
        case {'zqufh': 10, 'wergi': 4, 'mxeif': 93}:
            return (16, 34, 48)
        case _:
            return "default"


a = func((16, 34, 48))
b = func({'zqufh': 10, 'wergi': 4, 'mxeif': 93})
c = func('ndkhy')
