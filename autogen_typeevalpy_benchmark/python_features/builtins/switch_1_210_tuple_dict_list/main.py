#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (96, 58, 40):
            return {'pwdwb': 14, 'xpsai': 14, 'lwgcp': 22}
        case {'pwdwb': 14, 'xpsai': 14, 'lwgcp': 22}:
            return (96, 58, 40)
        case _:
            return "default"


a = func((96, 58, 40))
b = func({'pwdwb': 14, 'xpsai': 14, 'lwgcp': 22})
c = func([41, 1, 18])
