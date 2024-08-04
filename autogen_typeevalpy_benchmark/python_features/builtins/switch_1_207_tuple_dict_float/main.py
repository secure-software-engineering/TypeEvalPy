#  A function is defined with switch statement in it.
def func(value):
    match value:
        case (85, 50, 37):
            return {'epnlg': 1, 'siqqn': 8, 'mtodg': 60}
        case {'epnlg': 1, 'siqqn': 8, 'mtodg': 60}:
            return (85, 50, 37)
        case _:
            return "default"


a = func((85, 50, 37))
b = func({'epnlg': 1, 'siqqn': 8, 'mtodg': 60})
c = func(32.29)
