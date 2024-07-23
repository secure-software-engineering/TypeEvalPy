#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'aqvky': 47, 'hjaml': 93, 'ozptw': 96}:
            return 99
        case 99:
            return {'aqvky': 47, 'hjaml': 93, 'ozptw': 96}
        case _:
            return "default"


a = func({'aqvky': 47, 'hjaml': 93, 'ozptw': 96})
b = func(99)
c = func((52, 90, 10))
