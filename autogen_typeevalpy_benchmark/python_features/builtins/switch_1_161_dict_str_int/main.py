#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'zsqmd': 70, 'xykni': 41, 'mbqxx': 86}:
            return 'mbxet'
        case 'mbxet':
            return {'zsqmd': 70, 'xykni': 41, 'mbqxx': 86}
        case _:
            return "default"


a = func({'zsqmd': 70, 'xykni': 41, 'mbqxx': 86})
b = func('mbxet')
c = func(28)
