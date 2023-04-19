# Call on variable assigned to an attribute of an externally imported class.


from pycg_external_module.ext import Cls


def fn(a):
    return a()


a = Cls()

b = fn(a.fun)
