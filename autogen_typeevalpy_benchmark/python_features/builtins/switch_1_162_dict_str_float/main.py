#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'rpugh': 89, 'lvxpg': 30, 'xqraj': 57}:
            return 'nlgni'
        case 'nlgni':
            return {'rpugh': 89, 'lvxpg': 30, 'xqraj': 57}
        case _:
            return "default"


a = func({'rpugh': 89, 'lvxpg': 30, 'xqraj': 57})
b = func('nlgni')
c = func(67.41)
