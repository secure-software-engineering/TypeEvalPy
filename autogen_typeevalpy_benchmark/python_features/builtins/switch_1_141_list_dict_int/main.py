#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [45, 54, 59]:
            return {'ymjvg': 88, 'tmskh': 95, 'kpfcc': 40}
        case {'ymjvg': 88, 'tmskh': 95, 'kpfcc': 40}:
            return [45, 54, 59]
        case _:
            return "default"


a = func([45, 54, 59])
b = func({'ymjvg': 88, 'tmskh': 95, 'kpfcc': 40})
c = func(48)
