#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'sjxaj':
            return {'ygbtz': 77, 'jxfkc': 34, 'avagg': 26}
        case {'ygbtz': 77, 'jxfkc': 34, 'avagg': 26}:
            return 'sjxaj'
        case _:
            return "default"


a = func('sjxaj')
b = func({'ygbtz': 77, 'jxfkc': 34, 'avagg': 26})
c = func(66.62)
